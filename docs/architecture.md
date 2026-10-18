# Arquitectura Medallion

## Objetivo

Construir un pipeline reproducible e idempotente para analizar la evolución de
juegos en Steam y su asociación temporal con la exposición en Twitch. Bronze no
se reingesta durante el flujo normal: el pipeline lee las tablas existentes y
produce Silver, DLQ y Gold.

## Flujo lógico

```text
Bronze existente
    |
    | lectura con un cutoff común por corrida
    v
01_bronze_gate
    | contrato, perfilado, conteo en seco y audit
    v
silver_orquestator
    | schemas -> transformaciones SQL por tabla
    +----------------------+
    |                      |
    v                      v
Silver validado          DLQ rechazados
    |
    v
03_gold
    |
    v
Gold analítico
```

El coordinador `src/silver_orquestator` ejecuta los pasos de forma secuencial:

```text
crear_schemas -> games -> player_counts_monthly -> twitch_activity_monthly
```

El orquestador calcula el corte y ejecuta los notebooks de
`src/transformaciones/`. Gold queda fuera de esta entrega y debe consumir
únicamente las tablas Silver validadas.

## Capas y responsabilidades

### Bronze

Bronze contiene los datos raw cargados desde Kaggle mediante `kagglehub`.
Las tablas no se modifican en este pipeline. La ingesta diaria de
`steam_games` y `steam_games_review` es append; las fuentes de SteamCharts y
Twitch son cargas únicas según el plan.

### Bronze gate y audit

El orquestador no ejecuta la ingesta Bronze. Comprueba `run_ingestion=false`,
crea los esquemas de salida si faltan, calcula un único `cutoff_us` y pasa
todos los parámetros como strings a los notebooks Silver/DLQ.

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
- tipo de regla (`key` o `rule`);
- payload serializado;
- claves disponibles;
- hash y metadatos de Bronze, cutoff y corrida.

Los rechazados no deben mezclarse con `audit` ni entrar a Gold.

### Gold

Gold lee únicamente Silver validado. El alcance documentado en el plan es:

- `gold.game_growth`;
- `gold.twitch_steam_relationship`;
- `gold.dim_game` o `gold.game_health`, según D9.

El matching Twitch–Steam se resuelve en Gold a partir de nombres normalizados.
Los matches ambiguos se excluyen por defecto hasta que una decisión de la
compuerta indique otra política.

## Idempotencia

La idempotencia se basa en:

1. cutoff único por corrida;
2. `_row_hash` determinista, excluyendo metadatos de procesamiento;
3. `MERGE` en Silver por clave de negocio;
4. `CREATE OR REPLACE TABLE` en Silver y DLQ para reconstruir de forma
   determinista el estado completo visible hasta el cutoff;
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
