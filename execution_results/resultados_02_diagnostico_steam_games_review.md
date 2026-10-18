# Resultados del diagn?stico ? 02_diagnostico_steam_games_review

- **Notebook:** `02_diagnostico_steam_games_review`
- **Ejecutado:** `2026-10-18T22:14:49.910759+00:00` (zona horaria del driver)
- **Estado:** `completed`
- **Objetivo:** conservar los resultados efectivos de las validaciones SQL del notebook para su revisi?n local.

## Tablas inspeccionadas
- `steam_game_intelligence.bronze.steam_games_review`

## Consultas y resultados

### Consulta de celda SQL 1
_Filas exportadas: 1; m?ximo aplicado: 200._

| total_rows | distinct_app_ids | null_app_id_rows | missing_name_rows | null_reviews_rows | blank_reviews_rows | first_ingested_at | last_ingested_at |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 13501 | 13501 | 0 | 0 | 0 | 0 | 2026-10-18 22:13:25.283623 | 2026-10-18 22:13:25.283623 |

### Consulta de celda SQL 2
_Filas exportadas: 0; m?ximo aplicado: 200._

No se detectaron registros que incumplan esta validaci?n o la consulta no devolvi? filas.

### Consulta de celda SQL 3
_Filas exportadas: 0; m?ximo aplicado: 200._

No se detectaron registros que incumplan esta validaci?n o la consulta no devolvi? filas.

### Consulta de celda SQL 4
_Filas exportadas: 0; m?ximo aplicado: 200._

No se detectaron registros que incumplan esta validaci?n o la consulta no devolvi? filas.

### Consulta de celda SQL 5
_Filas exportadas: 1; m?ximo aplicado: 200._

| invalid_app_id | missing_ingestion_timestamp | blank_name | blank_reviews | blank_source |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 |

### Consulta de celda SQL 6
_Filas exportadas: 0; m?ximo aplicado: 200._

No se detectaron registros que incumplan esta validaci?n o la consulta no devolvi? filas.

### Muestra de estructura (una fila)
_Filas exportadas: 1; m?ximo aplicado: 200._

| app_id | name | reviews | _ingested_at | _source |
| --- | --- | --- | --- | --- |
| 1056840 | Arcanium: Rise of Akhan | “The game is genuinely really good and I can't recommend it enough” Alliestrasza, Pro Hearthstone streamer “This game is really good! This is on par with 'Slay the Spire', 'Monster Train' and 'Vault of the Void'.” Wanderbots, Youtube content creator “Arcanium is my favorite deckbuilder right now. You will love this game.” Regis Killbin, Pro Hearthstone streamer  | 2026-10-18 22:13:25.283623 | https://www.kaggle.com/datasets/hubertsidorowicz/steam-games-dataset-daily-updates |

## Hallazgos y conclusiones
Los hallazgos deben interpretarse a partir de los conteos y muestras exportados; esta celda no inventa conclusiones ni marca como aprobada una validaci?n no ejecutada.
