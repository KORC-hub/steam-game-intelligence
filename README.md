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
- La fuente `steam_game_reviews_batch` se valida en
  [`notebooks/data_validations/02_diagnostico_steam_games_review.ipynb`](./notebooks/data_validations/02_diagnostico_steam_games_review.ipynb)
  y se transforma en
  [`src/transformation/silver_game_reviews.ipynb`](./src/transformation/silver_game_reviews.ipynb),
  incluyendo perfilado del campo `reviews` y exportación Markdown.
- La carpeta [`notebooks/`](./notebooks/) contiene notebooks de consulta,
  validación y exportación de resultados; los informes se guardan en
  [`notebooks/data_validations/result_outputs/`](./notebooks/data_validations/result_outputs/)
  y no escribe las tablas Silver.
- Notebooks de transformación
  [`src/transformation/`](./src/transformation) para construir las cuatro
  tablas Silver y sus tablas DLQ.
- Notebook [`src/gold.ipynb`](./src/gold.ipynb) para construir `game_growth`,
  `twitch_steam_relationship` y `dim_game` exclusivamente desde Silver.
- Notebook de análisis
  [`notebooks/gold_analysis.ipynb`](./notebooks/gold_analysis.ipynb) para
  consultar Gold y responder las preguntas analíticas sin modificar tablas.
  Su última celda exporta los resultados a
  [`notebooks/data_validations/result_outputs/resultados_gold_analysis.md`](./notebooks/data_validations/result_outputs/resultados_gold_analysis.md).
- Notebook de pruebas
  [`notebooks/idempotency_tests.ipynb`](./notebooks/idempotency_tests.ipynb)
  para validar ejecuciones repetidas en esquemas sandbox sin modificar Bronze
  real.
- Orquestador
  [`notebooks/silver_orquestator.ipynb`](./notebooks/silver_orquestator.ipynb)
  con corte único de Bronze, ejecución de Silver/DLQ y Gold, y parámetros
  compatibles con un Job.
- Diagnósticos SQL para volumen, cobertura, nulos, duplicados, formatos,
  rangos, métricas inconsistentes, estado del batch actual y muestras de
  registros problemáticos.
- Documentación técnica de arquitectura, contrato de datos y validaciones
  Silver/DLQ en [`docs/`](./docs/).

### Implementado como código, pendiente de verificación en Databricks

- Flujo `Bronze → Silver → DLQ → Gold` mediante notebooks coordinados.
- Estandarización de nombres, tipos, listas y fechas en Silver.
- Validaciones de calidad aplicadas durante el procesamiento.
- Separación de filas aprobadas en Silver y filas rechazadas en DLQ.
- Escrituras Delta repetibles mediante `CREATE OR REPLACE TABLE` sobre el
  estado completo de las fuentes actuales.
- Esquemas y tablas creados dinámicamente a partir de parámetros de ejecución.
- Notebook Gold para crear `game_growth`, `twitch_steam_relationship` y
  `dim_game`, además del resumen `audit.match_quality`.
- Notebook de consultas Gold para comparar evolución de jugadores, exposición
  en Twitch y cambios posteriores en Steam.
- Notebook de idempotencia para comparar conteos, huellas, claves duplicadas e
  historial de Delta en Silver, DLQ y Gold.

La ejecución completa y las pruebas formales de idempotencia todavía deben
verificarse en Databricks. El repositorio contiene el código, pero no afirma
que todas las tablas existan o estén pobladas en el workspace.

## Fuentes de datos

| Fuente | Tabla Bronze | Carga | Cobertura conocida |
|---|---|---|---|
| Steam Games | `steam_games_batch` | Overwrite por batch | Catálogo y atributos de juegos |
| Steam Games Reviews | `steam_game_reviews_batch` | Overwrite por batch | Reviews en una estructura string aún no definida |
| SteamCharts | `steamcharts_player_counts_monthly` | Carga única | Histórico mensual de jugadores, 2012–2025 |
| Twitch Top 200 | `twitch_top_games_monthly` | Carga única | Actividad mensual, 2016–2024 |

Las tablas Bronze reales son las indicadas arriba. Algunos nombres antiguos que
aparecen en documentación previa (`steam_reviews`,
`steam_player_counts_monthly` y `twitch_top200_monthly`) no deben utilizarse
sin verificarlos contra el catálogo.

### Convención de nombres

Se adopta una convención de nombres en `snake_case` basada en tres elementos:

```text
<sistema_fuente>_<entidad>_<granularidad_o_estado>
```

En Bronze, el nombre conserva el sistema fuente y describe que la fuente se
recibe como un batch reemplazable o como una serie mensual:

- `steam_games_batch`
- `steam_game_reviews_batch`
- `steamcharts_player_counts_monthly`
- `twitch_top_games_monthly`

En Silver se usa el nombre de negocio normalizado:

- `silver.steam_games`
- `silver.steam_player_counts_monthly`
- `silver.twitch_game_activity_monthly`

Las tablas DLQ conservan el nombre lógico de Silver y agregan `_rejected`.
Gold mantiene nombres analíticos (`game_growth`,
`twitch_steam_relationship` y `dim_game`) porque no representa una fuente raw
sino productos del modelo.

La adquisición actual del proyecto se realiza mediante `kagglehub` desde
datasets de Kaggle; no se consumen APIs de Steam o Twitch en vivo. Si se
incorpora posteriormente una API directa, esta convención sigue siendo válida:
el sistema fuente identifica el origen y no el mecanismo de transporte. El
script de renombrado de objetos existentes está en
[`docs/rename-tables.sql`](./docs/rename-tables.sql).

### Particularidades conocidas

- `steam_games_batch` y `steam_game_reviews_batch` contienen el último batch
  disponible. La ingesta usa `overwrite`, por lo que no acumulan batches
  anteriores en Bronze.
- `steamcharts_player_counts_monthly` contiene `month` y `gain` como strings; su
  formato efectivo debe confirmarse antes de definir el parser.
- `twitch_top_games_monthly` no contiene `app_id`.
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

El alcance previsto contempla cuatro tablas principales:

| Tabla | Propósito |
|---|---|
| `silver.steam_games` | Estado vigente y atributos normalizados del catálogo |
| `silver.steam_player_counts_monthly` | Jugadores promedio y máximos por juego y mes |
| `silver.twitch_game_activity_monthly` | Actividad de Twitch por mes y posición del ranking |

Silver debe contener únicamente registros que hayan pasado las validaciones y
la deduplicación determinista. La implementación conserva una fila vigente
por juego en `games`, una fila por juego y mes en `player_counts_monthly` y
una fila por mes y posición en `twitch_activity_monthly`.

Las transformaciones que escriben tablas viven en
[`src/transformation/`](./src/transformation/). Cada notebook contiene una
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

### Gold implementado como código

El alcance implementado contempla:

- `gold.game_growth`: evolución mensual de jugadores y métricas de crecimiento.
- `gold.twitch_steam_relationship`: relación entre actividad de Twitch y
  jugadores de Steam cuando existe un match único.
- `gold.dim_game`: dimensión vigente del catálogo con `review_ratio`.

Gold debe construirse exclusivamente a partir de Silver validado.
La creación de estas tablas ocurre en `src/gold.ipynb`; las consultas para
responder las preguntas analíticas ocurren en
[`notebooks/gold_analysis.ipynb`](./notebooks/gold_analysis.ipynb).

## Unity Catalog

El catálogo utilizado por el proyecto es `steam_game_intelligence`. La
estructura objetivo es:

```text
steam_game_intelligence
├── bronze
│   ├── kaggle_data/                         # Volume de archivos de origen
│   ├── steam_games_batch
│   ├── steam_game_reviews_batch
│   ├── steamcharts_player_counts_monthly
│   └── twitch_top_games_monthly
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
│   └── dim_game
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
- [`docs/idempotency-testing.md`](./docs/idempotency-testing.md): procedimiento
  de aislamiento, ejecuciones repetidas y criterios de aceptación de
  idempotencia.

## Próximos pasos

1. Ejecutar el orquestador completo en Databricks y verificar Silver, DLQ y
   Gold.
2. Configurar el flujo completo mediante un Job sin activar la ingesta Bronze.
3. Ejecutar
   [`notebooks/idempotency_tests.ipynb`](./notebooks/idempotency_tests.ipynb)
   en Databricks para demostrar que Silver, DLQ y Gold no generan duplicados y
   reflejan las actualizaciones de Bronze sandbox.

Hasta completar esos pasos, las tablas y métricas de las capas posteriores
deben considerarse código preparado, no resultados publicados.

## Conclusiones del análisis Gold

Estas conclusiones corresponden a una ejecución de
[`notebooks/gold_analysis.ipynb`](./notebooks/gold_analysis.ipynb) generada el
19 de octubre de 2026 en UTC. Están escritas para explicar directamente qué
se observó en los datos. No demuestran que Twitch cause cambios en Steam.

### Cobertura analítica

- `gold.game_growth` tiene 605.537 registros de 6.693 juegos entre
  agosto de 2012 y septiembre de 2025.
- `gold.twitch_steam_relationship` tiene 9.042 registros de 1.191
  juegos entre enero de 2016 y septiembre de 2024.
- Para comparar Twitch con Steam solo se pudieron usar 5.182 registros de 458
  juegos. Por eso esta parte del análisis no representa a todos los juegos de
  las tablas Gold.

### Evolución de jugadores en Steam

- Al final del periodo, el promedio de jugadores por juego es mayor que al
  principio: sube de cerca de 400 jugadores en 2012 a cerca de 858 en
  septiembre de 2025.
- El promedio es mucho mayor que la mediana. Esto significa que unos pocos
  juegos tienen muchísimos jugadores y elevan el promedio. La mayoría de los
  juegos tiene menos jugadores.
- Algunos porcentajes de crecimiento son enormes porque el mes anterior tenía
  casi cero jugadores. Por ejemplo, *METAL GEAR RISING: REVENGEANCE* aparece
  con un crecimiento de `193.304%`. Ese porcentaje no significa que sea el juego
  que más jugadores ganó. Tampoco demuestra que Twitch haya causado el aumento.

### Relación entre Twitch y el crecimiento posterior en Steam

- La correlación entre las horas vistas en Twitch y el crecimiento posterior en
  Steam es `-0,0032`. Este número está muy cerca de cero. En estos datos no se
  ve una relación clara entre ambas medidas.
- El crecimiento promedio es `4,408%`, pero el crecimiento de la mitad central
  de los registros es aproximadamente `-0,0308%`. La diferencia ocurre porque
  algunos porcentajes muy grandes cambian mucho el promedio. Por eso la mediana
  describe mejor el resultado típico.
- Al ordenar los juegos desde los que tuvieron menos horas vistas hasta los que
  tuvieron más, los resultados no suben de forma ordenada:
  - grupo 1: crecimiento promedio de `3,600%`;
  - grupo 2: crecimiento promedio de `11,361%`;
  - grupo 3: crecimiento promedio de `0,324%`;
  - grupo 4: crecimiento promedio de `2,342%`.
- El segundo grupo tiene el promedio más alto, pero los grupos no aumentan uno
  tras otro. Por tanto, no se puede decir que más horas vistas en Twitch
  produzcan más crecimiento en Steam.

### Catálogo y reseñas

- `gold.dim_game` tiene 144.000 juegos y el precio medio observado es
  `8,983108`.
- Entre los juegos con reseñas válidas, la proporción promedio de reseñas
  positivas es `0,7581`.
- 60.929 juegos no tienen ese dato, aproximadamente el 42,3% del catálogo.
  No tener el dato no significa tener reseñas negativas.
- En esta ejecución todos los juegos aparecen como publicados. Por eso esta
  consulta no permitió comparar juegos publicados con juegos aún no publicados.

### Limitaciones e interpretación

Los porcentajes son poco confiables cuando el mes anterior tiene casi cero
jugadores. En una siguiente versión conviene mostrar también cuántos jugadores
se ganaron o perdieron en números absolutos y exigir un mínimo de jugadores
antes de calcular porcentajes.

También faltan datos que pueden explicar los cambios: fecha de lanzamiento,
promociones, temporadas y actualizaciones. La conclusión de este análisis es
solamente descriptiva: con los datos disponibles no se observa una relación
clara entre las horas vistas en Twitch y el crecimiento posterior en Steam.
