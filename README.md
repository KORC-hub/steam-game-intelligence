# Steam Game Intelligence

Proyecto de **Data Engineering y Big Data** para analizar la evolución, popularidad y longevidad de videojuegos mediante la integración de datos de **Steam, Twitch y otras fuentes externas**.

El proyecto busca estudiar la relación entre:

* Actividad de jugadores.
* Reviews y recepción de usuarios.
* Exposición en Twitch.
* Eventos como lanzamientos, updates y DLC.
* Evolución histórica de los videojuegos.

## Arquitectura

Se implementa una **Medallion Architecture** sobre Databricks:

```text
Fuentes externas
      │
      ▼
   ┌─────────┐
   │ Bronze  │  Raw / Ingestion
   └────┬────┘
        │
        ▼
   ┌─────────┐
   │ Silver  │  Cleaning / Standardization
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

Contiene los datos **raw** provenientes de las diferentes fuentes.

Los archivos externos se almacenan inicialmente en un **Unity Catalog Volume**:

```text
/Volumes/steam_game_intelligence/bronze/kaggle_data/
```

Posteriormente son procesados con Spark y almacenados como **Delta Tables**.

### Silver

Contiene los datos **cleaned, standardized e integrated**.

Se realizan procesos como:

* Limpieza de datos.
* Tratamiento de nulos y duplicados.
* Estandarización de schemas.
* Normalización de tipos y timestamps.
* Integración entre fuentes.

### Gold

Contiene los **analytical datasets** utilizados para generar métricas y realizar análisis.

Ejemplos:

```text
game_daily_metrics
game_growth
game_health
twitch_steam_relationship
```

## Unity Catalog

```text
steam_game_intelligence
│
├── bronze
│   ├── kaggle_data/       ← Volume
│   ├── steam_games
│   ├── steam_reviews
│   └── streaming_data
│
├── silver
│   ├── games
│   ├── reviews
│   ├── player_activity
│   └── streaming_activity
│
└── gold
    ├── game_daily_metrics
    ├── game_growth
    ├── game_health
    └── steaming_relationship
```

## Fuentes de datos

* **Kaggle** — datasets históricos y complementarios.

## Tecnologías

* **Databricks**
* **Apache Spark / PySpark**
* **Delta Lake**
* **Unity Catalog**
* **KaggleHub**
* **Steam API**
* **Twitch API**
* **GitHub**

## Objetivo analítico

El proyecto busca identificar patrones relacionados con el crecimiento, declive y longevidad de los videojuegos.

Una de las principales líneas de análisis es estudiar si existe una relación entre la exposición de un videojuego en Twitch y cambios posteriores en su actividad dentro de Steam.

> Las relaciones encontradas se interpretan como **associations**, no necesariamente como relaciones causales.
