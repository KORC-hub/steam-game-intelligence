# Resultados — Cuaderno ML 2: Random Forest de crecimiento

- Generado en UTC: 2026-11-25T04:17:32.614235+00:00
- Gold: `steam_game_intelligence.gold`
- Umbral de crecimiento: 10% | min_players=20.0
- Ventana: 2016-01-01 a 2024-08-01 | train hasta 2021-12-01
- Random Forest: numTrees=100, maxDepth=8, seed=42
- Géneros usados: ['{"id":"23","description":"Indie"}', '{"id":"1","description":"Action"}', '{"id":"25","description":"Adventure"}', '{"id":"2","description":"Strategy"}', '{"id":"3","description":"RPG"}', '{"id":"28","description":"Simulation"}', '{"id":"4","description":"Casual"}', '{"id":"37","description":"Free To Play"}']
- Pesos de clase: positivo=1.9674, negativo=0.6704
- PR-AUC al azar (tasa de positivos en test): 0.2140
- Diferencia de PR-AUC con Twitch vs. sin Twitch: -0.0021
- Importancia total de las variables de Twitch: 0.51%
- MLflow run ids: {'rf_sin_twitch': 'eb2d140caabc4be69eb478f237aff7fa', 'rf_con_twitch': 'f00d6cb3411149d3954dcc82c60f095b'}

## Volumetría de las tablas Gold

| tabla | filas | juegos |
| --- | --- | --- |
| game_growth | 605537 | 6693 |
| dim_game | 150848 | 150848 |
| twitch_steam_relationship | 5498 | 552 |

## Tasa de positivos según el umbral de crecimiento

| umbral_crecimiento | pct_filas_positivas |
| --- | --- |
| 5% | 31.63 |
| 10% | 24.14 |
| 20% | 15.16 |
| 30% | 10.34 |

## Balance de clases por conjunto

| conjunto | filas | juegos | positivos | pct_positivos |
| --- | --- | --- | --- | --- |
| train | 128623 | 3522 | 32689 | 25.41 |
| test | 60135 | 2686 | 12871 | 21.4 |

## Métricas en test (clase positiva = crecimiento ≥ umbral)

| modelo | pr_auc | roc_auc | precision_pos | recall_pos | f1_pos | accuracy | tp | fp | fn | tn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| referencia | 0.1816 | 0.4187 | 0.1794 | 0.22 | 0.1976 | 0.6176 | 2832 | 12955 | 10039 | 34309 |
| rf_sin_twitch | 0.4291 | 0.7228 | 0.3735 | 0.5862 | 0.4563 | 0.701 | 7545 | 12657 | 5326 | 34607 |
| rf_con_twitch | 0.427 | 0.7231 | 0.3773 | 0.5752 | 0.4557 | 0.7059 | 7404 | 12221 | 5467 | 35043 |

## Matriz de confusión en test (rf_sin_twitch)

|  | Predicho: no crece | Predicho: crece |
| --- | --- | --- |
| Real: no crece | 34607 | 12657 |
| Real: crece | 5326 | 7545 |

## Métricas en test solo con filas en el top 200 de Twitch (1,110 filas)

| modelo | pr_auc | roc_auc | precision_pos | recall_pos | f1_pos | accuracy | tp | fp | fn | tn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| referencia | 0.1892 | 0.4929 | 0.1952 | 0.2689 | 0.2262 | 0.6486 | 57 | 235 | 155 | 663 |
| rf_sin_twitch | 0.345 | 0.7061 | 0.3723 | 0.4057 | 0.3883 | 0.7559 | 86 | 145 | 126 | 753 |
| rf_con_twitch | 0.3626 | 0.7195 | 0.4008 | 0.4481 | 0.4232 | 0.7667 | 95 | 142 | 117 | 756 |

## Importancia de variables (rf_con_twitch)

| modelo | variable | importancia | es_twitch |
| --- | --- | --- | --- |
| rf_con_twitch | next_month | 0.248 | False |
| rf_con_twitch | next_month_is_steam_sale | 0.1728 | False |
| rf_con_twitch | log_change_3m | 0.1652 | False |
| rf_con_twitch | peak_to_avg_ratio | 0.1038 | False |
| rf_con_twitch | ratio_to_ma3 | 0.069 | False |
| rf_con_twitch | log_price | 0.0493 | False |
| rf_con_twitch | drawdown_from_peak | 0.047 | False |
| rf_con_twitch | log_change_1m | 0.0419 | False |
| rf_con_twitch | is_free | 0.0274 | False |
| rf_con_twitch | genre_id_37_description_free_to_play | 0.0202 | False |
| rf_con_twitch | log_avg_players | 0.0142 | False |
| rf_con_twitch | genre_id_25_description_adventure | 0.0063 | False |
| rf_con_twitch | genre_id_1_description_action | 0.0052 | False |
| rf_con_twitch | genre_id_2_description_strategy | 0.0047 | False |
| rf_con_twitch | has_lag_3m | 0.0043 | False |
| rf_con_twitch | genre_id_3_description_rpg | 0.0038 | False |
| rf_con_twitch | genre_id_23_description_indie | 0.0028 | False |
| rf_con_twitch | has_prev_month | 0.0026 | False |
| rf_con_twitch | log_hours_watched | 0.0025 | True |
| rf_con_twitch | genre_id_4_description_casual | 0.0023 | False |
| rf_con_twitch | has_catalog_info | 0.0022 | False |
| rf_con_twitch | genre_id_28_description_simulation | 0.0021 | False |
| rf_con_twitch | twitch_rank_filled | 0.0013 | True |
| rf_con_twitch | in_twitch_top200 | 0.0013 | True |
| rf_con_twitch | has_release_date | 0 | False |
| rf_con_twitch | months_since_release | 0 | False |

## Escenarios simulados (rf_con_twitch)

| escenario | jugadores_t | cambio_1m | drawdown_from_peak | months_since_release | in_twitch_top200 | probabilidad_crecimiento_pct | clasificacion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Juego mediano en caída, antes de las rebajas de verano | 3000 | -0.15 | 0.25 | 30 | 0 | 63.3 | CRECE ≥ umbral |
| Juego popular en el top 10 de Twitch | 40000 | 0.05 | 0.9 | 18 | 1 | 35.1 | NO CRECE |
| Lanzamiento reciente (segundo mes) | 5000 | -0.26 | 0.74 | 1 | 0 | 34.2 | NO CRECE |
| Juego gratuito estable y longevo | 15000 | 0.01 | 0.6 | 96 | 0 | 30.1 | NO CRECE |
| Juego pequeño con repunte reciente | 60 | 0.4 | 0.5 | 48 | 0 | 35 | NO CRECE |

## Gráficos guardados en plots/

| seccion | grafico | archivo |
| --- | --- | --- |
| 6.1 | distribucion crecimiento mensual | ml02_random_forest_sec06-1_distribucion_crecimiento_mensual.png |
| 7 | balance de clases | ml02_random_forest_sec07_balance_de_clases.png |
| 9 | comparacion de modelos | ml02_random_forest_sec09_comparacion_de_modelos.png |
| 9.1 | curvas precision recall | ml02_random_forest_sec09-1_curvas_precision_recall.png |
| 9.1 | matriz de confusion | ml02_random_forest_sec09-1_matriz_de_confusion.png |
| 10 | importancia de variables | ml02_random_forest_sec10_importancia_de_variables.png |
| 11 | escenarios simulados | ml02_random_forest_sec11_escenarios_simulados.png |
