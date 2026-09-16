# Steam Game Intelligence

Proyecto de **Data Engineering y Big Data** para analizar la evolución, popularidad y longevidad de videojuegos mediante la integración de datos de **Steam y Twitch** (ambos consumidos desde Kaggle).

El proyecto busca estudiar la relación entre:

* Catálogo y características de los juegos (precio, género, desarrollador, etc.).
* Reviews y recepción de usuarios.
* Cantidad de jugadores por mes en Steam.
* Exposición mensual en Twitch (Top 200 juegos).

> **Nota sobre esta versión del README:** reemplaza una versión anterior que hacía referencia a integraciones directas con la API de Steam y la API de Twitch. La implementación actual **no** consume esas APIs en vivo — todas las fuentes se obtienen desde **Kaggle vía `kagglehub`**. Si en el futuro se agrega una fuente en tiempo real, hay que actualizar esta sección y el diagrama de arquitectura.

## Fuentes de datos

Todas las fuentes se consumen desde Kaggle mediante `kagglehub` (`%pip install kagglehub` dentro del notebook de ingesta). Generan 4 tablas en la capa Bronze del catálogo `steam_game_intelligence`.

| # | Origen (Kaggle) | Tabla(s) Bronze | Cadencia de ingesta | Rango temporal |
|---|---|---|---|---|
| 1 | Steam Games Dataset (metadata de juegos + reviews) | `steam_games`, `steam_reviews` | **Diaria** — job programado, modo `append` | Snapshot diario acumulado desde el inicio del job |
| 2 | Cantidad de jugadores por mes en Steam | `steam_player_counts_monthly` | **Única** — descarga manual | 2012 – 2025 |
| 3 | Top 200 juegos mensuales en Twitch | `twitch_top200_monthly` | **Única** — descarga manual | 2016 – 2023 |

> El modo `append` en `steam_games` y `steam_reviews` permite construir un historial de snapshots diarios del catálogo de Steam, lo que habilita análisis de evolución en el tiempo (cambios de precio, actualización de metadata, nuevas reviews) en las capas Silver y Gold.

## Arquitectura

Se implementa una **Medallion Architecture** sobre Databricks:

```text
Kaggle (kagglehub)
      │
      ▼
   ┌─────────┐
   │ Bronze  │  Raw / Ingestion (append diario o carga única)
   └────┬────┘
        │
        ▼
   ┌─────────┐
   │ Silver  │  Cleaning / Standardization / Deduplicación de snapshots
   └────┬────┘
        │
        ▼
   ┌─────────┐
   │  Gold   │  Analytics / Metrics
   └────┬────┘
        │
        ▼
   Analytics / Dashboard
```

### Bronze

Datos **raw** provenientes de las 3 fuentes. Los archivos se descargan primero a un **Unity Catalog Volume**:

```text
/Volumes/steam_game_intelligence/bronze/kaggle_data/
```

y luego se procesan con Spark y se almacenan como **Delta Tables**.

### Silver

Datos **cleaned, standardized e integrated**. Incluye, entre otros pendientes:

* Deduplicación de los snapshots diarios de `steam_games` / `steam_reviews` (quedarse con el estado vigente y/o el histórico de cambios, según el caso de uso).
* Tratamiento de nulos y duplicados.
* Estandarización de schemas y timestamps.
* Resolución del cruce Steam ↔ Twitch por nombre de juego (no existe `app_id` común — ver sección de integración más abajo).

### Gold

Datasets analíticos:

```text
game_daily_metrics
game_growth
game_health
twitch_steam_relationship
```

## Unity Catalog

El catálogo `steam_game_intelligence` **ya existe** en el workspace.

```text
steam_game_intelligence
│
├── bronze
│   ├── kaggle_data/                    ← Volume (staging de archivos descargados)
│   ├── steam_games                     ← diaria, append
│   ├── steam_reviews                   ← diaria, append
│   ├── steam_player_counts_monthly     ← carga única
│   └── twitch_top200_monthly           ← carga única
│
├── silver
│   ├── games
│   ├── reviews
│   ├── player_counts_monthly
│   └── twitch_activity_monthly
│
└── gold
    ├── game_daily_metrics
    ├── game_growth
    ├── game_health
    └── twitch_steam_relationship
```

## Punto de integración entre fuentes

`steam_player_counts_monthly` y `twitch_top200_monthly` comparten granularidad **mensual**, lo que permite cruzarlas por año/mes. La unión a nivel de juego específico depende del **nombre del juego** (el dataset de Twitch no trae `app_id`), lo cual es una fuente de error conocida (nombres distintos, ediciones, remasters) y queda como trabajo pendiente para la capa Silver — no se resuelve en Bronze.

## Tecnologías

* **Databricks**
* **Apache Spark / PySpark**
* **Delta Lake**
* **Unity Catalog**
* **KaggleHub** — único mecanismo de ingesta actual

## Objetivo analítico

El proyecto busca identificar patrones relacionados con el crecimiento, declive y longevidad de los videojuegos.

Una de las principales líneas de análisis es estudiar si existe una relación entre la exposición de un videojuego en Twitch y cambios posteriores en la **cantidad de jugadores** de ese juego en Steam.

> Las relaciones encontradas se interpretan como **associations**, no necesariamente como relaciones causales.