# Resultados — Cuaderno ML 2: Random Forest de crecimiento

- Generado en UTC: 2026-11-25T02:26:16.293881+00:00
- Gold: `steam_game_intelligence.gold`
- Umbral de crecimiento: 10% | min_players=20.0
- Ventana: 2016-01-01 a 2024-08-01 | train hasta 2021-12-01
- Random Forest: numTrees=100, maxDepth=8, seed=42
- Géneros usados: []
- Pesos de clase: positivo=1.9674, negativo=0.6704
- PR-AUC al azar (tasa de positivos en test): 0.2140
- Diferencia de PR-AUC con Twitch vs. sin Twitch: +0.0006
- Importancia total de las variables de Twitch: 0.63%
- MLflow run ids: {'rf_sin_twitch': 'c8310e8c9cfd491aacfed78665cc9080', 'rf_con_twitch': 'd39d1fc6b3744c6699b87ec66e2ff708'}

## Volumetría de las tablas Gold

| tabla | filas | juegos |
| --- | --- | --- |
| game_growth | 605537 | 6693 |
| dim_game | 0 | 0 |
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
| rf_sin_twitch | 0.4102 | 0.7156 | 0.3739 | 0.5557 | 0.447 | 0.7058 | 7152 | 11974 | 5719 | 35290 |
| rf_con_twitch | 0.4108 | 0.7163 | 0.3751 | 0.5483 | 0.4454 | 0.7078 | 7057 | 11759 | 5814 | 35505 |

## Matriz de confusión en test (rf_con_twitch)

|  | Predicho: no crece | Predicho: crece |
| --- | --- | --- |
| Real: no crece | 35505 | 11759 |
| Real: crece | 5814 | 7057 |

## Métricas en test solo con filas en el top 200 de Twitch (1,110 filas)

| modelo | pr_auc | roc_auc | precision_pos | recall_pos | f1_pos | accuracy | tp | fp | fn | tn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| referencia | 0.1892 | 0.4929 | 0.1952 | 0.2689 | 0.2262 | 0.6486 | 57 | 235 | 155 | 663 |
| rf_sin_twitch | 0.3321 | 0.681 | 0.3299 | 0.3019 | 0.3153 | 0.7495 | 64 | 130 | 148 | 768 |
| rf_con_twitch | 0.3338 | 0.6934 | 0.3301 | 0.3255 | 0.3278 | 0.745 | 69 | 140 | 143 | 758 |

## Importancia de variables (rf_con_twitch)

| modelo | variable | importancia | es_twitch |
| --- | --- | --- | --- |
| rf_con_twitch | next_month | 0.2789 | False |
| rf_con_twitch | log_change_3m | 0.1879 | False |
| rf_con_twitch | next_month_is_steam_sale | 0.1854 | False |
| rf_con_twitch | peak_to_avg_ratio | 0.1422 | False |
| rf_con_twitch | ratio_to_ma3 | 0.0698 | False |
| rf_con_twitch | drawdown_from_peak | 0.053 | False |
| rf_con_twitch | log_change_1m | 0.0481 | False |
| rf_con_twitch | log_avg_players | 0.0175 | False |
| rf_con_twitch | has_lag_3m | 0.0073 | False |
| rf_con_twitch | has_prev_month | 0.0036 | False |
| rf_con_twitch | log_hours_watched | 0.0031 | True |
| rf_con_twitch | in_twitch_top200 | 0.0017 | True |
| rf_con_twitch | twitch_rank_filled | 0.0015 | True |
| rf_con_twitch | log_price | 0 | False |
| rf_con_twitch | has_catalog_info | 0 | False |
| rf_con_twitch | is_free | 0 | False |
| rf_con_twitch | months_since_release | 0 | False |
| rf_con_twitch | has_release_date | 0 | False |

## Escenarios simulados (rf_con_twitch)

| escenario | jugadores_t | cambio_1m | drawdown_from_peak | months_since_release | in_twitch_top200 | probabilidad_crecimiento_pct | clasificacion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Juego mediano en caída, antes de las rebajas de verano | 3000 | -0.15 | 0.25 | 30 | 0 | 45.6 | NO CRECE |
| Juego popular en el top 10 de Twitch | 40000 | 0.05 | 0.9 | 18 | 1 | 32.4 | NO CRECE |
| Lanzamiento reciente (segundo mes) | 5000 | -0.26 | 0.74 | 1 | 0 | 28.9 | NO CRECE |
| Juego gratuito estable y longevo | 15000 | 0.01 | 0.6 | 96 | 0 | 30.3 | NO CRECE |
| Juego pequeño con repunte reciente | 60 | 0.4 | 0.5 | 48 | 0 | 34.2 | NO CRECE |

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
