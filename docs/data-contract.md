# Contrato de datos y fuentes

Este documento resume el contrato que debe verificar `01_bronze_gate`. Los
tipos indicados son el contrato esperado descrito en [PLAN.md](../PLAN.md),
no sustituyen la verificación contra `printSchema()` o `DESCRIBE` en Databricks.

## Fuentes Bronze

| Tabla | Carga | Clave natural esperada | Particularidades |
|---|---|---|---|
| `steam_games` | append diario | `app_id` + `_ingested_at` | `estimated_owners`, `genres`, `categories` y `tags` son strings; algunos valores numéricos fueron inferidos como `double` |
| `steam_games_review` | append diario | `app_id` + `_ingested_at` | `reviews` es un string de estructura aún no definida; está fuera del alcance Silver/Gold provisional |
| `steamcharts_2025_history_data` | carga única | `(steam_appid, month)` | `month` y `gain` son strings; sus formatos deben medirse antes de decidir el parser |
| `twitch_top_200_games_data` | carga única | `(Year, Month, Rank)` | nombres en PascalCase; no contiene `app_id`; el enlace con Steam es por nombre |

Las tablas reales del repositorio son las anteriores. El README contiene
nombres históricos (`steam_reviews`, `steam_player_counts_monthly` y
`twitch_top200_monthly`) que no deben usarse para implementar el pipeline sin
verificación. El plan y los notebooks de diagnóstico usan los nombres reales.

## Campos de control

Todas las fuentes esperadas incluyen:

- `_ingested_at`: timestamp de llegada y límite para el cutoff;
- `_source`: procedencia de la fila.

No existe `_batch_id`. Por eso el lote se identifica mediante `_ingested_at` y
el coordinador debe calcular un cutoff único para toda la corrida.

## Transformación prevista hacia Silver

### `steam_games` -> `silver.games`

Se espera conservar los atributos usados por Gold: identificación, nombre,
fecha, precio, propietarios, desarrolladores, publicadores, listas
descriptivas, reviews, actividad y disponibilidad. Se descartan de Silver
campos descriptivos pesados que no usa Gold, según la sección 9.1 de
[PLAN.md](../PLAN.md).

Transformaciones que requieren decisión:

- parsing de `estimated_owners` (D10);
- separador de `genres`, `categories` y `tags` (D3);
- semántica de cero en puntuaciones (D4);
- elección de tipos para valores `double` que conceptualmente son enteros.

### `steamcharts_2025_history_data` -> `silver.player_counts_monthly`

Se espera producir:

- `app_id` desde `steam_appid`;
- `month_start` como fecha del primer día del mes;
- `avg_players`, `peak_players`;
- `gain` y `gain_percent`, sujetos a D1 y D2;
- `name` y `name_norm`;
- `in_catalog`, sujeto a D5.

### `twitch_top_200_games_data` -> `silver.twitch_activity_monthly`

Se espera estandarizar:

- `Year` -> `year`;
- `Month` -> `month`;
- `Rank` -> `twitch_rank`;
- `Game` -> `game`;
- `game_name_norm` para el matching posterior;
- métricas de audiencia y emisión a nombres snake_case.

La ausencia de correspondencia con Steam no es un rechazo DQL de Twitch. El top
200 puede incluir categorías o juegos que no existan en Steam; esa diferencia se
resuelve con columnas de matching en Gold.

## Convenciones de conversión

Sobre Bronze se deben usar `try_cast`, `try_to_date` y `try_divide`. Una
conversión que no pueda realizarse debe producir una señal que pueda ir a DQL,
no tumbar silenciosamente el Job ni inventar un valor.

Los hashes de comparación no incluyen `_ingested_at`, `_source`, `_processed_at`
ni `_run_id`. Así, los metadatos de ejecución no convierten una fila sin
cambios en una actualización.

## Pendientes de verificación

Los siguientes valores no están fijados en esta documentación:

- formato efectivo de `month`;
- patrones efectivos de `gain`;
- cantidad de snapshots distintos de `steam_games`;
- proporción de huérfanos SteamCharts;
- proporción de matches únicos, ambiguos y ausentes Twitch–Steam;
- semántica de ceros;
- existencia de valores no enteros en columnas inferidas como `double`.

Estos datos deben venir del perfilado ejecutado, no de supuestos.
