# Steam Game Intelligence

Proyecto de **Data Engineering y Big Data** para analizar la evolución,
popularidad y longevidad de videojuegos a partir de datos de Steam y Twitch.
Las fuentes se obtienen desde Kaggle mediante `kagglehub`; el proyecto no
consume las APIs de Steam o Twitch en tiempo real.

La pregunta analítica principal es:

> ¿Existe una asociación entre la exposición mensual de un videojuego en Twitch
> y cambios posteriores en la cantidad de jugadores de ese juego en Steam?

Los resultados se interpretan como **asociaciones**, no como relaciones
causales.

## Estado del proyecto

### Implementado

- Repositorio organizado para trabajar con Databricks, Spark, Delta Lake y
  Unity Catalog.
- Catálogo de trabajo definido como `steam_game_intelligence`.
- Capa Bronze existente con tablas Delta y un Volume para los archivos de
  Kaggle.
- Notebooks de ingesta para las fuentes de SteamCharts, Steam Games y Twitch.
- Cuatro notebooks de diagnóstico en
  [`notebooks/data_validations/`](./notebooks/data_validations/).
- La carpeta [`notebooks/`](./notebooks/) contiene notebooks de consulta,
  validación y exportación de resultados; no escribe las tablas Silver.
- Notebook de transformación
  [`src/transformaciones/`](./src/transformaciones) para construir las tres
  tablas Silver y sus tablas DLQ.
- Orquestador
  [`src/silver_orquestator.ipynb`](./src/silver_orquestator.ipynb) con corte
  único de Bronze y parámetros compatibles con un Job.
- Diagnósticos SQL para volumen, cobertura, nulos, duplicados, formatos,
  rangos, métricas inconsistentes, variaciones entre snapshots y muestras de
  registros problemáticos.
- Documentación técnica de arquitectura, contrato de datos y validaciones
  Silver/DLQ en [`docs/`](./docs/).

### Implementado como código, pendiente de ejecución

- Flujo `Bronze → Silver → DLQ` mediante notebooks coordinados.
- Estandarización de nombres, tipos, listas y fechas en Silver.
- Validaciones de calidad aplicadas durante el procesamiento.
- Separación de filas aprobadas en Silver y filas rechazadas en DLQ.
- Escrituras Delta repetibles mediante `CREATE OR REPLACE TABLE` sobre el
  estado completo de las fuentes actuales.
- Esquemas y tablas creados dinámicamente a partir de parámetros de ejecución.

La ejecución real de estos notebooks todavía debe verificarse en Databricks.
El repositorio contiene el código, pero no afirma que las tablas ya existan en
el workspace.

### En diseño

- Tablas Gold para crecimiento de jugadores, relación Twitch–Steam y una
  dimensión o métrica de estado del juego.

Gold, el Job y las pruebas formales de idempotencia todavía requieren
implementación o validación en Databricks.

## Fuentes de datos

| Fuente | Tabla Bronze | Carga | Cobertura conocida |
|---|---|---|---|
| Steam Games | `steam_games` | Append de snapshots | Catálogo y atributos de juegos |
| Steam Games Reviews | `steam_games_review` | Append de snapshots | Reviews en una estructura string aún no definida |
| SteamCharts | `steamcharts_2025_history_data` | Carga única | Histórico mensual de jugadores, 2012–2025 |
| Twitch Top 200 | `twitch_top_200_games_data` | Carga única | Actividad mensual, 2016–2024 |

Las tablas Bronze reales son las indicadas arriba. Algunos nombres antiguos que
aparecen en documentación previa (`steam_reviews`,
`steam_player_counts_monthly` y `twitch_top200_monthly`) no deben utilizarse
sin verificarlos contra el catálogo.

### Particularidades conocidas

- `steam_games` y `steam_games_review` pueden contener snapshots diarios.
- `steamcharts_2025_history_data` contiene `month` y `gain` como strings; su
  formato efectivo debe confirmarse antes de definir el parser.
- `twitch_top_200_games_data` no contiene `app_id`.
- El cruce Twitch–Steam depende de nombres normalizados y puede producir
  coincidencias únicas, ambiguas o inexistentes.
- La ausencia de un juego de Twitch en Steam no se considera por sí sola un
  rechazo de calidad.

## Arquitectura

```text
Kaggle / kagglehub
        |
        v
Bronze existente
        |
        v
Diagnóstico y contrato de Bronze
        |
        v
Silver validado ---------> DLQ: filas rechazadas
        |
        v
Gold analítico
        |
        v
Análisis de evolución y asociación Twitch–Steam
```

### Bronze

Bronze conserva los datos de origen y se trata como una capa de solo lectura
para las transformaciones. Los archivos descargados se almacenan en el Volume
de Unity Catalog:

```text
/Volumes/steam_game_intelligence/bronze/kaggle_data/
```

### Diagnóstico

Los notebooks actuales son:

- [`01_diagnostico_steam_games.ipynb`](./notebooks/data_validations/01_diagnostico_steam_games.ipynb)
- [`02_diagnostico_steam_games_review.ipynb`](./notebooks/data_validations/02_diagnostico_steam_games_review.ipynb)
- [`03_diagnostico_steamcharts_history.ipynb`](./notebooks/data_validations/03_diagnostico_steamcharts_history.ipynb)
- [`04_diagnostico_twitch_top200.ipynb`](./notebooks/data_validations/04_diagnostico_twitch_top200.ipynb)

Estos notebooks consultan Bronze sin modificarlo. Sus resultados sirven para
conocer la calidad y la forma real de los datos antes de fijar las reglas de
Silver y DLQ.

### Silver

El alcance previsto contempla tres tablas principales:

| Tabla | Propósito |
|---|---|
| `silver.games` | Estado vigente y atributos normalizados del catálogo |
| `silver.player_counts_monthly` | Jugadores promedio y máximos por juego y mes |
| `silver.twitch_activity_monthly` | Actividad de Twitch por mes y posición del ranking |

Silver debe contener únicamente registros que hayan pasado las validaciones y
la deduplicación determinista. La implementación conserva una fila vigente
por juego en `games`, una fila por juego y mes en `player_counts_monthly` y
una fila por mes y posición en `twitch_activity_monthly`.

Las transformaciones que escriben tablas viven en
[`src/transformaciones/`](./src/transformaciones/). Cada notebook contiene una
sección SQL para Silver y otra para DLQ.

### DLQ

DLQ es una capa independiente para conservar registros rechazados durante el
procesamiento de Silver. Cada rechazo debe incluir un `motivo_rechazo` y la
trazabilidad necesaria para identificar la regla incumplida y la fila de
origen.

Las validaciones implementadas incluyen claves inválidas, fechas no parseables,
valores negativos, rangos imposibles, nombres vacíos, conversiones de `gain` y
duplicados conflictivos. Los rechazos conservan `motivo_rechazo`, reglas,
payload y metadatos de corrida.

### Gold

El alcance previsto contempla:

- `gold.game_growth`: evolución mensual de jugadores y métricas de crecimiento.
- `gold.twitch_steam_relationship`: relación entre actividad de Twitch y
  jugadores de Steam cuando existe un match único.
- Una tercera tabla de dimensión o estado del juego, cuya definición se
  completará junto con la fórmula correspondiente.

Gold debe construirse exclusivamente a partir de Silver validado.

## Unity Catalog

El catálogo utilizado por el proyecto es `steam_game_intelligence`. La
estructura objetivo es:

```text
steam_game_intelligence
├── bronze
│   ├── kaggle_data/                         # Volume de archivos de origen
│   ├── steam_games
│   ├── steam_games_review
│   ├── steamcharts_2025_history_data
│   └── twitch_top_200_games_data
├── silver
│   ├── games
│   ├── player_counts_monthly
│   └── twitch_activity_monthly
├── dlq
│   ├── games_rejected
│   ├── player_counts_monthly_rejected
│   └── twitch_activity_monthly_rejected
├── gold
│   ├── game_growth
│   ├── twitch_steam_relationship
│   └── <tercera tabla Gold>
└── audit
```

La existencia y el esquema efectivo de cada objeto deben verificarse en el
workspace antes de ejecutar transformaciones que escriban datos.

## Tecnologías

- Databricks
- Apache Spark y PySpark
- Spark SQL
- Delta Lake
- Unity Catalog
- KaggleHub
- Git/GitHub para versionado y sincronización del código

## Documentación técnica

La descripción detallada se encuentra en:

- [`docs/architecture.md`](./docs/architecture.md): arquitectura, capas,
  dependencias e idempotencia.
- [`docs/data-contract.md`](./docs/data-contract.md): fuentes, granularidad,
  campos relevantes y transformaciones previstas.
- [`docs/silver-dlq-validations.md`](./docs/silver-dlq-validations.md):
  validaciones, deduplicación, estructura DLQ y contabilidad.

## Próximos pasos

1. Ejecutar el orquestador en Databricks y verificar la creación de Silver/DLQ.
2. Construir Gold únicamente desde Silver.
3. Configurar el flujo completo mediante un Job sin activar la ingesta Bronze.
4. Ejecutar pruebas repetidas que demuestren que Silver, DLQ y Gold no generan
   duplicados y reflejan las actualizaciones de Bronze.

Hasta completar esos pasos, las tablas y métricas de las capas posteriores
deben considerarse código preparado, no resultados publicados.
