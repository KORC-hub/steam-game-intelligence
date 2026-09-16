# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %md
# MAGIC # Steam Game Intelligence — Entrega 1 - Capa Bronze

# COMMAND ----------

# MAGIC %md
# MAGIC ## Sección 1 — Contexto de Negocio y Resumen de Datos
# MAGIC
# MAGIC ### 1.1 Justificación del dominio
# MAGIC
# MAGIC El proyecto integra 3 fuentes de datos de Kaggle relacionadas con el ecosistema de videojuegos
# MAGIC en Steam y Twitch. Cada fuente aporta una dimensión distinta y complementaria del mismo fenómeno
# MAGIC (el ciclo de vida de un videojuego):
# MAGIC
# MAGIC | Fuente | Qué aporta | Por qué es necesaria |
# MAGIC |---|---|---|
# MAGIC | Steam Games + Reviews | Catálogo (precio, género, desarrollador) y percepción de usuarios (reviews) | Sin esto no hay contexto de *qué es* el juego ni cómo lo reciben los usuarios |
# MAGIC | Cantidad de jugadores por mes en Steam | Actividad real de consumo, medida en cantidad de jugadores | Es la variable de "salud"/longevidad del juego que se quiere explicar |
# MAGIC | Top 200 juegos mensuales en Twitch | Exposición mediática / atención pública | Es la variable candidata a explicar cambios posteriores en la actividad de Steam |
# MAGIC
# MAGIC **Hipótesis de negocio:** existe una asociación entre la exposición de un juego en Twitch y
# MAGIC cambios posteriores en su cantidad de jugadores en Steam. Se interpreta como **asociación, no
# MAGIC causalidad**.
# MAGIC
# MAGIC **Nota** el dataset de Twitch no trae `app_id` de
# MAGIC Steam, por lo que el cruce entre fuentes dependerá de *matching* por nombre de juego en Silver.

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1.2 Ficha técnica por fuente
# MAGIC
# MAGIC #### Fuente 1 — Steam Games Dataset (juegos + reviews)
# MAGIC
# MAGIC | Campo | Valor |
# MAGIC |---|---|
# MAGIC | Origen | Kaggle (dataset actualizado a diario) |
# MAGIC | Método de extracción | `kagglehub` (`%pip install kagglehub`) → descarga a Volume → `spark.read` → tabla Delta |
# MAGIC | Cadencia | Diaria, job de Databricks Workflows, modo `append` |
# MAGIC | Volumen exacto | 153916 |
# MAGIC | Tablas Bronze resultantes | `steam_games`, `steam_games_review` (unidas por `app_id`) |
# MAGIC
# MAGIC #### Fuente 2 — Cantidad de jugadores por mes en Steam
# MAGIC
# MAGIC | Campo | Valor |
# MAGIC |---|---|
# MAGIC | Origen | Kaggle (histórico estático) |
# MAGIC | Método de extracción | `kagglehub`, descarga manual única → Volume → `spark.read` → tabla Delta |
# MAGIC | Cadencia | Única (no se re-ingesta) |
# MAGIC | Rango temporal | 2012 – 2025 |
# MAGIC | Volumen exacto | 612265 |
# MAGIC | Tabla Bronze | `steamcharts_2025_history_data` |
# MAGIC
# MAGIC #### Fuente 3 — Top 200 juegos mensuales en Twitch
# MAGIC
# MAGIC | Campo | Valor |
# MAGIC |---|---|
# MAGIC | Origen | Kaggle (histórico estático) |
# MAGIC | Método de extracción | `kagglehub`, descarga manual única → Volume → `spark.read` → tabla Delta |
# MAGIC | Cadencia | Única (no se re-ingesta) |
# MAGIC | Rango temporal | 2016 – 2023 |
# MAGIC | Volumen exacto | 21000 |
# MAGIC | Tabla Bronze | `twitch_top_200_games_data` |
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1.3 Volumetría real

# COMMAND ----------

BRONZE_SCHEMA = "steam_game_intelligence.bronze"

bronze_tables = [
    "steam_games",
    "steam_games_review",
    "steamcharts_2025_history_data",
    "twitch_top_200_games_data",
]

for table_name in bronze_tables:
    full_name = f"{BRONZE_SCHEMA}.{table_name}"
    df = spark.table(full_name)
    row_count = df.count()
    # DESCRIBE DETAIL da el tamaño real en disco (sizeInBytes) de la tabla Delta
    size_info = spark.sql(f"DESCRIBE DETAIL {full_name}").select("sizeInBytes", "numFiles").first()
    print(f"{full_name}: {row_count:,} registros | {size_info['sizeInBytes'] / (1024**2):.2f} MB | {size_info['numFiles']} archivos")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Sección 2 — Diagrama de Arquitectura Inicial
# MAGIC
# MAGIC Diagrama en Mermaid. Si tu runtime de Databricks no renderiza Mermaid en celdas `%md`, copia el
# MAGIC bloque en [mermaid.live](https://mermaid.live) o reconstrúyelo en draw.io como respaldo.

# COMMAND ----------

# MAGIC %md
# MAGIC ![Arquitectura](./resources/Diagrama_Arquitectura_Inicial.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Sección 3 — Pipeline de Ingesta (resumen — implementación ya existente)
# MAGIC
# MAGIC Esta sección se documenta de forma breve porque el pipeline ya está construido y corriendo en
# MAGIC producción.
# MAGIC
# MAGIC | Fuente | Mecanismo | Modo de carga | Campos de auditoría |
# MAGIC |---|---|---|---|
# MAGIC | `steam_games` / `steam_reviews` | `kagglehub` + job diario en Databricks Workflows | `append` | `_ingested_at`, `_source` |
# MAGIC | `steam_player_counts_monthly` | `kagglehub`, descarga manual | carga única | `_ingested_at`, `_source` |
# MAGIC | `twitch_top200_monthly` | `kagglehub`, descarga manual | carga única | `_ingested_at`, `_source` |
# MAGIC
# MAGIC El modo `append` en `steam_games` y `steam_reviews` permite construir un historial de snapshots
# MAGIC diarios del catálogo de Steam, habilitando análisis de evolución en el tiempo (cambios de precio,
# MAGIC actualización de metadata, nuevas reviews) en las capas Silver y Gold.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Sección 4 — Validaciones Iniciales y Detección de Anomalías / Atípicos
# MAGIC
# MAGIC Diagnóstico exploratorio **sin modificar la data cruda de Bronze**. El objetivo es documentar
# MAGIC hallazgos para la futura Capa Silver, no corregirlos aquí.
# MAGIC
# MAGIC Ajusta `BRONZE_SCHEMA` y los nombres de columnas placeholder (`[PLACEHOLDER]`) a tu schema real
# MAGIC antes de correr estas celdas.

# COMMAND ----------

from pyspark.sql import functions as F

BRONZE_SCHEMA = "steam_game_intelligence.bronze"

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4.1 Conteo total de registros por tabla

# COMMAND ----------

for table_name in bronze_tables:
    full_name = f"{BRONZE_SCHEMA}.{table_name}"
    total = spark.table(full_name).count()
    print(f"{full_name}: {total:,} registros totales")
    # → [PLACEHOLDER] pegar aquí el resultado real como comentario o en un markdown de hallazgos

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4.2 Conteo de nulos por columna
# MAGIC
# MAGIC Genérico: aplica a cualquier tabla, sin necesidad de listar columnas a mano.

# COMMAND ----------

def null_counts(df):
    """Devuelve un DataFrame con el conteo de nulos por columna."""
    return df.select([
        F.count(F.when(F.col(c).isNull(), c)).alias(c)
        for c in df.columns
    ])


for table_name in bronze_tables:
    full_name = f"{BRONZE_SCHEMA}.{table_name}"
    df = spark.table(full_name)

    null_df = null_counts(df)
    null_values = null_df.collect()[0].asDict()

    # Columnas con más de 1 nulo
    columns_with_nulls = {
        column: count
        for column, count in null_values.items()
        if count > 1
    }

    if columns_with_nulls:
        print(f"--- {full_name} ---")

        # Nulos por columna
        for column, count in columns_with_nulls.items():
            print(f"{column}: {count} nulos")

        # Total de nulos de la tabla
        total_nulls = sum(null_values.values())

        print(f"TOTAL: {total_nulls} nulos")
        print()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4.3 Duplicados exactos y por clave natural

# COMMAND ----------

# Duplicados exactos (todas las columnas iguales) — aplica a las 4 tablas
for table_name in bronze_tables:
    full_name = f"{BRONZE_SCHEMA}.{table_name}"
    df = spark.table(full_name)
    total = df.count()
    unique_total = df.dropDuplicates().count()
    print(f"{full_name}: {total - unique_total:,} filas exactamente duplicadas")

# COMMAND ----------

# Duplicados por clave natural en steam_games — dentro de un mismo snapshot diario
# (si existe _ingested_at, agrupar por fecha; si no existe todavía, este check no se puede
# hacer correctamente y es evidencia de que falta el campo de auditoría — ver Sección 3)

steam_games_df = spark.table(f"{BRONZE_SCHEMA}.steam_games")

dup_por_snapshot = (
    steam_games_df
    .groupBy(F.col("_ingested_at").cast("date").alias("snapshot_date"), "app_id")
    .count()
    .filter(F.col("count") > 1)
)
print(f"app_id duplicados dentro del mismo snapshot diario: {dup_por_snapshot.count():,}")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4.4 Outliers / valores atípicos específicos del dominio

# COMMAND ----------

# --- steam_games: fechas de lanzamiento futuras y precios negativos ---
games_df = spark.table(f"{BRONZE_SCHEMA}.steam_games")

future_releases = games_df.filter(F.col("release_date") > F.current_date())
print(f"Juegos con fecha de lanzamiento futura: {future_releases.count():,}")

negative_price = games_df.filter(F.col("price") < 0)
print(f"Juegos con precio negativo: {negative_price.count():,}")

# COMMAND ----------

# --- steam_player_counts_monthly: valores negativos e inconsistencia peak < avg ---
# [PLACEHOLDER: ajustar nombres de columna reales — avg_players / peak_players son propuestos]

players_df = spark.table(f"{BRONZE_SCHEMA}.steamcharts_2025_history_data")

negative_players = players_df.filter(
    (F.col("avg_players") < 0) | (F.col("peak_players") < 0)
)
print(f"Registros con jugadores negativos: {negative_players.count():,}")

peak_menor_que_avg = players_df.filter(F.col("peak_players") < F.col("avg_players"))
print(f"Registros donde el pico de jugadores es menor al promedio (inconsistencia lógica): "
      f"{peak_menor_que_avg.count():,}")

# COMMAND ----------

# --- twitch_top200_monthly: rank fuera de rango y horas negativas ---
# [PLACEHOLDER: ajustar nombres de columna reales]

twitch_df = spark.table(f"{BRONZE_SCHEMA}.twitch_top_200_games_data")

rank_fuera_de_rango = twitch_df.filter((F.col("rank") < 1) | (F.col("rank") > 200))
print(f"Registros con rank fuera de 1-200: {rank_fuera_de_rango.count():,}")

horas_negativas = twitch_df.filter(
    (F.col("hours_watched") < 0) | (F.col("hours_streamed") < 0)
)
print(f"Registros con horas negativas: {horas_negativas.count():,}")

# COMMAND ----------

# --- Integridad referencial: reviews sin juego asociado en steam_games ---
reviews_df = spark.table(f"{BRONZE_SCHEMA}.steam_games_review")

reviews_huerfanas = reviews_df.join(games_df.select("app_id"), on="app_id", how="left_anti")
print(f"Reviews con app_id que no existe en steam_games: {reviews_huerfanas.count():,}")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4.5 Resumen de hallazgos (completar con resultados reales)
# MAGIC
# MAGIC | Tabla | Registros totales | % nulos (columna crítica) | Duplicados exactos | Outliers detectados |
# MAGIC |---|---|---|---|---|
# MAGIC | steam_games | 140,940 | price: 0.87% (1,230), metacritic_score: 29.6% | 0 | 0 fechas futuras, 0 precios negativos |
# MAGIC | steam_reviews | 13,205 | 0% | 0 | 0 reviews huérfanas |
# MAGIC | steam_player_counts_monthly | 612,265 | 0% | 0 | 0 negativos, 0 peak<avg |
# MAGIC | twitch_top200_monthly | 21,000 | 0% | 0 | 0 rank inválido, 0 horas negativas |
# MAGIC