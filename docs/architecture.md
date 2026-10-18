# Arquitectura Medallion

## Objetivo

Construir un pipeline reproducible e idempotente para analizar la evolución de
juegos en Steam y su asociación temporal con la exposición en Twitch. Bronze no
se reingesta durante el flujo normal: el pipeline lee las tablas existentes y
produce Silver, DQL y Gold.

## Flujo lógico

```text
Bronze existente
    |
    | lectura con un cutoff común por corrida
    v
01_bronze_gate
    | contrato, perfilado, conteo en seco y audit
    v
02_silver_dql
    | staging tipado -> reglas de clave -> deduplicación -> reglas de negocio
    +----------------------+
    |                      |
    v                      v
Silver validado          DQL rechazados
    |
    v
03_gold
    |
    v
Gold analítico
```

El coordinador `00_orchestrator` ejecuta los pasos de forma secuencial:

```text
bronze_gate -> silver_dql -> gold
```

La Fase 1 implementa solamente `bronze_gate`. Los notebooks de Silver y Gold se
construyen después de completar la compuerta D1–D12.

## Capas y responsabilidades

### Bronze

Bronze contiene los datos raw cargados desde Kaggle mediante `kagglehub`.
Las tablas no se modifican en este pipeline. La ingesta diaria de
`steam_games` y `steam_games_review` es append; las fuentes de SteamCharts y
Twitch son cargas únicas según el plan.

### Bronze gate y audit

`01_bronze_gate`:

1. Comprueba existencia, contenido, columnas y tipos esperados.
2. Calcula un único cutoff por tabla a partir de `_ingested_at`.
3. Perfila volumen, lotes, formatos, ceros, cruces y reglas candidatas.
4. Persiste las mediciones en `audit`.
5. Devuelve un reporte compacto y falla si el contrato tiene un `FAIL`.

Una sonda que falle debe registrar el error y continuar con las demás sondas.
Esto permite distinguir un problema de datos de un problema de la consulta de
perfilado.

### Silver

El alcance acordado es:

| Tabla | Grano |
|---|---|
| `silver.games` | un `app_id` vigente al cutoff |
| `silver.player_counts_monthly` | `(app_id, month_start)` |
| `silver.twitch_activity_monthly` | `(month_start, twitch_rank)` |

Silver estandariza nombres, tipos y fechas; normaliza nombres para el matching;
aplica reglas de clave y negocio; y conserva solamente filas aprobadas.

### DQL

DQL es un esquema independiente. Cada tabla Silver tiene una tabla de
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
4. `MERGE` en DQL por `_reject_key`;
5. `WHEN NOT MATCHED BY SOURCE THEN DELETE` para reflejar el estado validado
   del cutoff;
6. `INSERT OVERWRITE` para Gold;
7. contabilidad de filas antes y después de escribir.

La prueba de aceptación debe demostrar que dos ejecuciones con el mismo cutoff:

- no duplican Silver;
- no duplican DQL;
- no duplican Gold;
- reflejan una actualización de Bronze correctamente;
- producen las mismas métricas de perfilado.

## Parametrización

El catálogo y los esquemas (`bronze`, `silver`, `dql`, `gold`, `audit`) deben
recibirse por widgets/configuración. No se deben dispersar nombres de tres
niveles dentro de SQL fijo cuando el nombre depende del entorno.

Los notebooks coordinados reciben todos los argumentos como strings. Los hijos
no calculan otro cutoff: usan el `cutoff_json` recibido del coordinador.
