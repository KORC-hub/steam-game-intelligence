# Resultados del diagn?stico ? 01_diagnostico_steam_games

- **Notebook:** `01_diagnostico_steam_games`
- **Ejecutado:** `2026-10-18T22:14:22.466192+00:00` (zona horaria del driver)
- **Estado:** `completed`
- **Objetivo:** conservar los resultados efectivos de las validaciones SQL del notebook para su revisi?n local.

## Tablas inspeccionadas
- `steam_game_intelligence.bronze.steam_games`

## Consultas y resultados

### Consulta de celda SQL 1
_Filas exportadas: 1; m?ximo aplicado: 200._

| total_rows | distinct_app_ids | first_ingested_at | last_ingested_at | null_app_id_rows | missing_name_rows |
| --- | --- | --- | --- | --- | --- |
| 144015 | 144015 | 2026-10-18 22:13:02.740734 | 2026-10-18 22:13:02.740734 | 0 | 15 |

### Consulta de celda SQL 2
_Filas exportadas: 25; m?ximo aplicado: 200._

| column_name | null_count |
| --- | --- |
| notes | 117212 |
| metacritic_score | 49102 |
| full_audio_languages | 41580 |
| recommendations | 41006 |
| achievements | 21407 |
| about_the_game | 8425 |
| detailed_description | 8405 |
| short_description | 8331 |
| price | 1337 |
| release_date | 82 |
| supported_languages | 26 |
| name | 15 |
| windows | 14 |
| mac | 14 |
| linux | 14 |
| estimated_owners | 1 |
| tags | 1 |
| positive | 1 |
| negative | 1 |
| peak_ccu | 1 |
| user_score | 1 |
| average_playtime_forever | 1 |
| median_playtime_forever | 1 |
| average_playtime_2weeks | 1 |
| median_playtime_2weeks | 1 |

### Consulta de celda SQL 3
_Filas exportadas: 0; m?ximo aplicado: 200._

No se detectaron registros que incumplan esta validaci?n o la consulta no devolvi? filas.

### Consulta de celda SQL 4
_Filas exportadas: 0; m?ximo aplicado: 200._

No se detectaron registros que incumplan esta validaci?n o la consulta no devolvi? filas.

### Consulta de celda SQL 5
_Filas exportadas: 1; m?ximo aplicado: 200._

| invalid_app_id | negative_price | negative_positive_reviews | negative_negative_reviews | negative_recommendations | negative_peak_ccu | metacritic_out_of_range | user_score_out_of_range | negative_achievements | negative_dlc_count | future_release_date | missing_ingestion_timestamp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

### Consulta de celda SQL 6
_Filas exportadas: 15; m?ximo aplicado: 200._

| app_id | name | release_date | price | positive | negative | recommendations | peak_ccu | metacritic_score | user_score | achievements | dlc_count | _ingested_at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 396420 | NULL | 2016-11-01 | 0.0 | 28 | 14 | NULL | 0 | NULL | 0 | NULL | 0 | 2026-10-18 22:13:02.740734 |
| 4226130 | NULL | NULL | NULL | 0 | 0 | NULL | 0 | NULL | 0 | NULL | 0 | 2026-10-18 22:13:02.740734 |
| 3839710 | NULL | NULL | NULL | 0 | 0 | NULL | 0 | NULL | 0 | NULL | 0 | 2026-10-18 22:13:02.740734 |
| 4161640 | NULL | NULL | NULL | 0 | 0 | NULL | 0 | NULL | 0 | NULL | 0 | 2026-10-18 22:13:02.740734 |
| 4337680 | NULL | NULL | NULL | 0 | 0 | NULL | 0 | NULL | 0 | NULL | 0 | 2026-10-18 22:13:02.740734 |
| 4304230 | NULL | NULL | NULL | 0 | 0 | NULL | 0 | NULL | 0 | NULL | 0 | 2026-10-18 22:13:02.740734 |
| 4190600 | NULL | NULL | NULL | 0 | 0 | NULL | 0 | NULL | 0 | NULL | 0 | 2026-10-18 22:13:02.740734 |
| 4207050 | NULL | NULL | NULL | 0 | 0 | NULL | 0 | NULL | 0 | NULL | 0 | 2026-10-18 22:13:02.740734 |
| 4073960 | NULL | NULL | NULL | 0 | 0 | NULL | 0 | NULL | 0 | NULL | 0 | 2026-10-18 22:13:02.740734 |
| 4113810 | NULL | NULL | NULL | 0 | 0 | NULL | 0 | NULL | 0 | NULL | 0 | 2026-10-18 22:13:02.740734 |
| 4243760 | NULL | NULL | NULL | 0 | 0 | NULL | 0 | NULL | 0 | NULL | 0 | 2026-10-18 22:13:02.740734 |
| 4279820 | NULL | NULL | NULL | 0 | 0 | NULL | 0 | NULL | 0 | NULL | 0 | 2026-10-18 22:13:02.740734 |
| 4284560 | NULL | NULL | NULL | 0 | 0 | NULL | 0 | NULL | 0 | NULL | 0 | 2026-10-18 22:13:02.740734 |
| 4517110 | NULL | NULL | NULL | 0 | 0 | NULL | 0 | NULL | 0 | NULL | 0 | 2026-10-18 22:13:02.740734 |
| 4073890 | NULL | NULL | NULL | 0 | 0 | NULL | 0 | NULL | 0 | NULL | 0 | 2026-10-18 22:13:02.740734 |

### Consulta de celda SQL 7
_Filas exportadas: 1; m?ximo aplicado: 200._

| blank_name | blank_developers | blank_publishers | blank_genres | blank_categories | blank_source |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 | 0 |

### Consulta de celda SQL 8
_Filas exportadas: 0; m?ximo aplicado: 200._

No se detectaron registros que incumplan esta validaci?n o la consulta no devolvi? filas.

### Muestra de estructura (una fila)
_Filas exportadas: 1; m?ximo aplicado: 200._

| app_id | name | release_date | price | price_status | estimated_owners | developers | publishers | genres | categories | tags | positive | negative | recommendations | peak_ccu | metacritic_score | user_score | average_playtime_forever | median_playtime_forever | average_playtime_2weeks | median_playtime_2weeks | short_description | about_the_game | detailed_description | notes | achievements | dlc_count | packages | supported_languages | full_audio_languages | windows | mac | linux | header_image | screenshots | movies | website | support_url | support_email | metacritic_url | steam_store_available | steam_spy_available | _ingested_at | _source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1056080 | Epic Adventures: Cursed Onboard | 2019-04-11 | 7.99 | paid | 0 - 20000 | ["Urchin Games"] | ["HH-Games"] | ["Action", "Adventure", "Casual", "Indie", "Strategy"] | ["Single-player", "Family Sharing"] | ["Adventure", "Casual", "Action", "Indie", "Strategy", "Hidden Object", "Mouse only"] | 20 | 12 | 0.0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | Play this great hidden object adventure, that takes you to a derelict ship stranded in the middle of the Great Amazon jungle. The recently discovered ship set sail in the 1970s but it never reached its destination. There were no survivors and the fate of the whole crew still remains a mystery. | The sequel of Epic Adventures, 'Epic Adventures: Cursed Onboard' takes you to a derelict ship stranded in the middle of the Great Amazon jungle. The recently discovered ship set sail in the 1970s but it never reached its destination. There were no survivors and the fate of the whole crew still remains a mystery. With the help of the ghost of a little girl named Anna, you will search the ship in detail and uncover a story that is astonishing as well as tragic! Dive into this incredible hidden object adventure game!  | The sequel of Epic Adventures, 'Epic Adventures: Cursed Onboard' takes you to a derelict ship stranded in the middle of the Great Amazon jungle. The recently discovered ship set sail in the 1970s but it never reached its destination. There were no survivors and the fate of the whole crew still remains a mystery. With the help of the ghost of a little girl named Anna, you will search the ship in detail and uncover a story that is astonishing as well as tragic! Dive into this incredible hidden object adventure game!  | NULL | 0.0 | 0 | [{"title": "Buy Epic Adventures: Cursed Onboard", "description": "", "subs": [{"text": "Epic Adventures: Cursed Onboard - $7.99 $5.19", "description": "", "price": 5.19}]}] | ["German", "English"] | [] | True | False | False | https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1056080/header.jpg?t=1728922946 | ["https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1056080/ss_3cefc0a0412078821347ba49bf6491466c440e91.1920x1080.jpg?t=1728922946", "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1056080/ss_43c02eac7b418500b18be9077deb289b13744421.1920x1080.jpg?t=1728922946", "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1056080/ss_c56ebcc1f023a21b3db4c64d8ec846b2c1a84421.1920x1080.jpg?t=1728922946", "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1056080/ss_4c19c77b0d580ac00b69db7f51a0d70dc26384c7.1920x1080.jpg?t=1728922946", "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1056080/ss_b043eb8ea053beead3680a6012a964c33f39fad6.1920x1080.jpg?t=1728922946", "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1056080/ss_8db830c864adad0304b5393967dbde7889088a9a.1920x1080.jpg?t=1728922946", "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1056080/ss_663fbb2a9e441bb9a9f151438f106136cd6fb36d.1920x1080.jpg?t=1728922946"] | [] | NULL | NULL | support@gamepublishing.de | NULL | True | True | 2026-10-18 22:13:02.740734 | https://www.kaggle.com/datasets/hubertsidorowicz/steam-games-dataset-daily-updates |

## Hallazgos y conclusiones
Los hallazgos deben interpretarse a partir de los conteos y muestras exportados; esta celda no inventa conclusiones ni marca como aprobada una validaci?n no ejecutada.
