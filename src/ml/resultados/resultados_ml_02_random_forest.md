# Resultados — Cuaderno ML 2: Random Forest de crecimiento

- Generado en UTC: 2026-11-25T04:40:11.892708+00:00
- Gold: `steam_game_intelligence.gold`
- Umbral de crecimiento: 10% | min_players=20.0
- Ventana: 2016-01-01 a 2024-08-01 | train hasta 2021-12-01
- Random Forest: numTrees=100, maxDepth=8, seed=42
- Géneros usados: ['Indie', 'Action', 'Adventure', 'Strategy', 'RPG', 'Simulation', 'Casual', 'Free To Play']
- Pesos de clase: positivo=1.9674, negativo=0.6704
- PR-AUC al azar (tasa de positivos en test): 0.2140
- Diferencia de PR-AUC con Twitch vs. sin Twitch: -0.0017
- Importancia total de las variables de Twitch: 0.47%
- MLflow run ids: {'rf_sin_twitch': '13cd9346e9e04fcfb009dc9e2d41d050', 'rf_con_twitch': '62eb81f42f454743a94966a9e49a271f'}

## Volumetría de las tablas Gold

| tabla | filas | juegos |
| --- | --- | --- |
| game_growth | 605537 | 6693 |
| dim_game | 150848 | 150848 |
| twitch_steam_relationship | 9102 | 1191 |

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
| rf_sin_twitch | 0.4287 | 0.7236 | 0.3775 | 0.5828 | 0.4582 | 0.705 | 7501 | 12370 | 5370 | 34894 |
| rf_con_twitch | 0.427 | 0.7235 | 0.3797 | 0.5692 | 0.4555 | 0.7088 | 7326 | 11968 | 5545 | 35296 |

## Matriz de confusión en test (rf_sin_twitch)

|  | Predicho: no crece | Predicho: crece |
| --- | --- | --- |
| Real: no crece | 34894 | 12370 |
| Real: crece | 5370 | 7501 |

## Métricas en test solo con filas en el top 200 de Twitch (1,132 filas)

| modelo | pr_auc | roc_auc | precision_pos | recall_pos | f1_pos | accuracy | tp | fp | fn | tn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| referencia | 0.1873 | 0.496 | 0.1946 | 0.2723 | 0.227 | 0.6511 | 58 | 240 | 155 | 679 |
| rf_sin_twitch | 0.3491 | 0.7112 | 0.3863 | 0.4225 | 0.4036 | 0.765 | 90 | 143 | 123 | 776 |
| rf_con_twitch | 0.3552 | 0.7125 | 0.3827 | 0.4366 | 0.4079 | 0.7615 | 93 | 150 | 120 | 769 |

## Importancia de variables (rf_con_twitch)

| modelo | variable | importancia | es_twitch |
| --- | --- | --- | --- |
| rf_con_twitch | next_month | 0.2445 | False |
| rf_con_twitch | next_month_is_steam_sale | 0.1719 | False |
| rf_con_twitch | log_change_3m | 0.1658 | False |
| rf_con_twitch | peak_to_avg_ratio | 0.1005 | False |
| rf_con_twitch | ratio_to_ma3 | 0.0648 | False |
| rf_con_twitch | log_price | 0.0464 | False |
| rf_con_twitch | drawdown_from_peak | 0.0463 | False |
| rf_con_twitch | log_change_1m | 0.0396 | False |
| rf_con_twitch | is_free | 0.0273 | False |
| rf_con_twitch | months_since_release | 0.0219 | False |
| rf_con_twitch | genre_free_to_play | 0.0197 | False |
| rf_con_twitch | log_avg_players | 0.0122 | False |
| rf_con_twitch | genre_adventure | 0.0058 | False |
| rf_con_twitch | genre_action | 0.0049 | False |
| rf_con_twitch | has_lag_3m | 0.0041 | False |
| rf_con_twitch | genre_rpg | 0.0039 | False |
| rf_con_twitch | genre_strategy | 0.0036 | False |
| rf_con_twitch | genre_indie | 0.0026 | False |
| rf_con_twitch | has_prev_month | 0.0024 | False |
| rf_con_twitch | log_hours_watched | 0.0023 | True |
| rf_con_twitch | genre_simulation | 0.002 | False |
| rf_con_twitch | has_release_date | 0.0019 | False |
| rf_con_twitch | genre_casual | 0.0017 | False |
| rf_con_twitch | has_catalog_info | 0.0016 | False |
| rf_con_twitch | twitch_rank_filled | 0.0012 | True |
| rf_con_twitch | in_twitch_top200 | 0.0011 | True |

## Escenarios simulados (rf_con_twitch)

| escenario | jugadores_t | cambio_1m | drawdown_from_peak | months_since_release | in_twitch_top200 | probabilidad_crecimiento_pct | clasificacion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Juego mediano en caída, antes de las rebajas de verano | 3000 | -0.15 | 0.25 | 30 | 0 | 65.3 | CRECE ≥ umbral |
| Juego popular en el top 10 de Twitch | 40000 | 0.05 | 0.9 | 18 | 1 | 35.6 | NO CRECE |
| Lanzamiento reciente (segundo mes) | 5000 | -0.26 | 0.74 | 1 | 0 | 34.3 | NO CRECE |
| Juego gratuito estable y longevo | 15000 | 0.01 | 0.6 | 96 | 0 | 28 | NO CRECE |
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
