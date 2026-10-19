# Arquitectura Medallion

## Objetivo

Construir un pipeline reproducible e idempotente para analizar la evolución de
juegos en Steam y su asociación temporal con la exposición en Twitch. Bronze no
se reingesta durante el flujo normal: el pipeline lee las tablas existentes y
produce Silver, DLQ y Gold.

## Flujo lógico

```text
bronze existente
    | contrato y perfilado mediante diagnósticos
    v
notebooks/silver_orquestator
    | schemas -> transformaciones SQL por tabla
    +----------------------+
    |                      |
    v                      v
Silver validado          DLQ rechazados
    |
    v
src/gold
    |
    v
Gold analítico
```

El coordinador `notebooks/silver_orquestator.ipynb` ejecuta los pasos de forma secuencial:

```text
crear_schemas -> games -> player_counts_monthly -> twitch_activity_monthly -> gold
```

La creación de tablas pertenece a `src/`. Los notebooks de `notebooks/` son de
diagnóstico o consulta. En particular,
[`notebooks/gold_analysis.ipynb`](../notebooks/gold_analysis.ipynb) consulta
Gold para responder las preguntas analíticas y no escribe tablas.


## Capas y responsabilidades

### Bronze

Bronze contiene los datos raw cargados desde Kaggle mediante `kagglehub`.
Las tablas no se modifican en este pipeline. La ingesta diaria de
`steam_games` y `steam_games_review` es append; las fuentes de SteamCharts y
Twitch son cargas únicas según el plan.

### Bronze y audit

El orquestador no ejecuta la ingesta Bronze. Comprueba `run_ingestion=false`,
crea los esquemas de salida si faltan, calcula un único `cutoff_us` y pasa
todos los parámetros como strings a los notebooks Silver/DLQ y Gold.

### Silver

El alcance acordado es:

| Tabla | Grano |
|---|---|
| `silver.games` | un `app_id` vigente al cutoff |
| `silver.player_counts_monthly` | `(app_id, month_start)` |
| `silver.twitch_activity_monthly` | `(month_start, twitch_rank)` |

Silver estandariza nombres, tipos y fechas; normaliza nombres para el matching;
aplica reglas de clave y negocio; y conserva solamente filas aprobadas.

### DLQ

DLQ es un esquema independiente. Cada tabla Silver tiene una tabla de
rechazados correspondiente. Un registro rechazado se conserva una sola vez por
`_reject_key` y contiene:

- `motivo_rechazo`;
- `reglas_violadas`;
- payload serializado;
- `_reject_key`;
- `_run_id` y `_rejected_at`.

Los rechazados no deben mezclarse con `audit` ni entrar a Gold.

### Gold

Gold lee únicamente Silver validado. El alcance documentado en el plan es:

- `gold.game_growth`;
- `gold.twitch_steam_relationship`;
- `gold.dim_game`, según la decisión confirmada.

También se crea `audit.match_quality` con el conteo de matches únicos,
ambiguos y ausentes, ponderado por filas y horas vistas.

Las consultas descriptivas sobre estas tablas se ejecutan en
`notebooks/gold_analysis.ipynb`. Sus resultados representan asociaciones y no
causalidad.

El matching Twitch–Steam se resuelve en Gold a partir de nombres normalizados.
Los matches ambiguos se excluyen por defecto hasta que una decisión de la
compuerta indique otra política.

## Idempotencia

La idempotencia se basa en:

1. cutoff único por corrida;
2. `_row_hash` determinista, excluyendo metadatos de procesamiento;
3. `MERGE` en Silver por clave de negocio;
4. `CREATE OR REPLACE TABLE` en Silver y DLQ para reconstruir de forma
   determinista el estado completo visible hasta el cutoff. Esta es la
   estrategia implementada actualmente; el plan original proponía `MERGE`.
5. `INSERT OVERWRITE` para Gold;
6. contabilidad de filas antes y después de escribir.

La prueba de aceptación debe demostrar que dos ejecuciones con el mismo cutoff:

- no duplican Silver;
- no duplican DLQ;
- no duplican Gold;
- reflejan una actualización de Bronze correctamente;
- producen las mismas métricas de perfilado.

## Parametrización

El catálogo y los esquemas (`bronze`, `silver`, `dlq`, `gold`, `audit`) deben
recibirse por widgets/configuración. No se deben dispersar nombres de tres
niveles dentro de SQL fijo cuando el nombre depende del entorno.

Los notebooks coordinados reciben todos los argumentos como strings. Los hijos no calculan otro cutoff: usan el `cutoff_us` recibido del orquestador.
