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
- Cinco notebooks de diagnóstico en
  [`notebooks/data_validations/`](./notebooks/data_validations/).
- Notebook específico de validación para `steam_games_review` en
  [`notebooks/data_validations/05_validacion_steam_games_review.ipynb`](./notebooks/data_validations/05_validacion_steam_games_review.ipynb),
  incluyendo perfilado del campo `reviews` y exportación Markdown.
- La carpeta [`notebooks/`](./notebooks/) contiene notebooks de consulta,
  validación y exportación de resultados; los informes se guardan en
  [`notebooks/data_validations/result_outputs/`](./notebooks/data_validations/result_outputs/)
  y no escribe las tablas Silver.
- Notebooks de transformación
  [`src/transformation/`](./src/transformation) para construir las tres
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
  rangos, métricas inconsistentes, variaciones entre snapshots y muestras de
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
19 de octubre de 2026 en UTC. Describen asociaciones observadas en los datos;
no demuestran que la exposición en Twitch cause cambios en los jugadores de
Steam.

### Cobertura analítica

- `gold.game_growth` contiene 605.537 observaciones de 6.693 juegos entre
  agosto de 2012 y septiembre de 2025.
- `gold.twitch_steam_relationship` contiene 9.042 observaciones de 1.191
  juegos entre enero de 2016 y septiembre de 2024.
- La asociación Twitch-Steam se pudo calcular con jugadores válidos para 5.182
  observaciones y 458 juegos. Por tanto, esta conclusión utiliza una muestra
  menor que el total de juegos presentes en Gold.

### Evolución de jugadores en Steam

- La media mensual de jugadores por juego aumenta en términos generales hacia
  el final de la ventana observada: pasa de valores cercanos a 400 en 2012 a
  valores cercanos a 858 en septiembre de 2025.
- La mediana mensual permanece muy por debajo de la media durante todo el
  periodo. Esto indica una distribución sesgada: pocos juegos concentran
  grandes cantidades de jugadores, mientras muchos juegos tienen comunidades
  pequeñas.
- Los mayores crecimientos porcentuales están dominados por juegos cuyo valor
  anterior era cercano a cero. Por eso aparecen porcentajes muy elevados,
  como 193.304% para *METAL GEAR RISING: REVENGEANCE*. Estos valores no deben
  interpretarse directamente como los mayores incrementos absolutos ni como
  evidencia de un efecto de Twitch.

### Relación entre Twitch y el crecimiento posterior en Steam

- La correlación entre `hours_watched` en Twitch y el crecimiento posterior de
  jugadores en Steam es `-0,0032`, prácticamente nula en la muestra analizada.
- La media del crecimiento posterior es `4,408%`, pero la mediana es
  `-0,0308%`. La diferencia muestra que la media está influida por
  observaciones extremas; la mediana representa mejor el comportamiento típico
  de la muestra.
- El análisis por cuartiles no presenta una tendencia monotónica:
  - cuartil 1: crecimiento medio de `3,600%`;
  - cuartil 2: crecimiento medio de `11,361%`;
  - cuartil 3: crecimiento medio de `0,324%`;
  - cuartil 4: crecimiento medio de `2,342%`.
- El segundo cuartil presenta la mayor media, pero esto no permite afirmar que
  una mayor exposición produzca mayor crecimiento. La falta de orden creciente
  entre cuartiles y la correlación cercana a cero no respaldan una relación
  lineal global.

### Catálogo y reseñas

- `gold.dim_game` contiene 144.000 juegos y el precio medio observado es
  `8,983108`.
- La proporción media de reseñas positivas es `0,7581` entre los juegos que
  tienen reseñas válidas.
- 60.929 juegos no tienen `review_ratio`, aproximadamente el 42,3% del
  catálogo. Esta ausencia debe considerarse al interpretar la valoración
  agregada y no debe confundirse con una proporción de reseñas negativa.
- En esta ejecución todos los registros tienen `is_unreleased = false`; por
  tanto, no se observó una separación efectiva entre juegos publicados y no
  publicados en la consulta de catálogo.

### Limitaciones e interpretación

Los cambios porcentuales son inestables cuando el valor del mes anterior es
igual o cercano a cero. Para un análisis posterior sería recomendable
complementarlos con cambios absolutos, umbrales mínimos de jugadores y medidas
robustas como medianas o percentiles. También sería necesario controlar por
fecha de lanzamiento, promociones, estacionalidad, actualizaciones y otros
factores antes de realizar una inferencia causal. Con los resultados actuales,
la conclusión principal es que no se observa una asociación lineal relevante
entre las horas vistas en Twitch y el crecimiento posterior de jugadores en
Steam.
