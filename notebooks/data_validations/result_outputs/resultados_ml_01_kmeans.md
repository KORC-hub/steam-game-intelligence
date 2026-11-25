# Resultados — Cuaderno ML 1: K-Means de ciclos de vida

- Generado en UTC: 2026-11-25T00:45:38.199229+00:00
- Gold: `steam_game_intelligence.gold`
- Umbrales: min_months=12, min_peak_players=20.0
- Juegos en el modelo: 4,007 (descartados por nulos: 0)
- k elegido: 3 (mayor silueta entre los k que cumplen el tamaño mínimo) | silueta final: 0.4794
- Varianza explicada por PCA 2D: 33.5% + 28.6%
- Pares de variables con |r| > 0,85: ninguno

## Volumetría de las tablas Gold

| tabla | filas | juegos |
| --- | --- | --- |
| game_growth | 605537 | 6693 |
| dim_game | 0 | 0 |
| twitch_steam_relationship | 5498 | 552 |

## Juegos que cumplen cada combinación de umbrales

| historial | pico >= 0 | pico >= 20 | pico >= 50 | pico >= 100 |
| --- | --- | --- | --- | --- |
| meses >= 6 | 6530 | 4013 | 3165 | 2465 |
| meses >= 12 | 6369 | 4007 | 3162 | 2463 |
| meses >= 24 | 6030 | 3988 | 3148 | 2453 |

## Estadísticos de las variables de entrada

| summary | log_peak_players | months_observed | pct_time_to_peak | retention_ratio | trend_slope_yearly | volatility | log_peak_to_avg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| count | 4007 | 4007 | 4007 | 4007 | 4007 | 4007 | 4007 |
| mean | 5.459789268740612 | 110.55003743448964 | 0.2937243385703541 | 0.19327408749550873 | -0.04484638722863619 | 0.3823156161127428 | 1.268759157601713 |
| stddev | 1.7396672614758395 | 32.76220972087977 | 0.3211971555219972 | 0.21060364265614 | 0.21978216122480299 | 0.22319436596708406 | 0.6674477390057105 |
| min | 3.044998514856909 | 12.0 | 0.0 | 6.29588820717541E-5 | -3.1084770523493384 | 0.039958515410059355 | 0.1827192233785484 |
| 25% | 4.1067670822206574 | 91.0 | 0.019230769230769232 | 0.042233787029623694 | -0.16647073021449316 | 0.2272775556531229 | 0.8573471182600421 |
| 50% | 5.114334430427416 | 110.0 | 0.15178571428571427 | 0.10630202140309156 | -0.055808818189225284 | 0.33862738702991324 | 1.0871787299951494 |
| 75% | 6.4846963024729245 | 137.0 | 0.52 | 0.27872498146775393 | 0.06634015458631908 | 0.4755858975919266 | 1.393309597115702 |
| max | 14.276024155215566 | 158.0 | 1.0 | 0.9850563878945631 | 1.0033543233086277 | 1.8018776355416997 | 4.042975298959619 |

## Matriz de correlación de las variables de entrada

| variable | log_peak_players | months_observed | pct_time_to_peak | retention_ratio | trend_slope_yearly | volatility | log_peak_to_avg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| log_peak_players | 1 | 0.14 | 0.02 | 0.01 | 0.03 | -0 | -0.33 |
| months_observed | 0.14 | 1 | -0.07 | 0.04 | -0.01 | -0.36 | -0.43 |
| pct_time_to_peak | 0.02 | -0.07 | 1 | 0.56 | 0.61 | 0.17 | 0.24 |
| retention_ratio | 0.01 | 0.04 | 0.56 | 1 | 0.52 | -0.23 | -0.15 |
| trend_slope_yearly | 0.03 | -0.01 | 0.61 | 0.52 | 1 | 0.2 | 0.22 |
| volatility | -0 | -0.36 | 0.17 | -0.23 | 0.2 | 1 | 0.74 |
| log_peak_to_avg | -0.33 | -0.43 | 0.24 | -0.15 | 0.22 | 0.74 | 1 |

## Evaluación de k (silueta, inercia y tamaño mínimo)

| k | silhouette | inercia | min_cluster_share | tamanos | cumple_tamano_minimo |
| --- | --- | --- | --- | --- | --- |
| 3 | 0.4794 | 16906.4 | 0.1168 | [2628, 911, 468] | True |
| 4 | 0.3212 | 14966.5 | 0.1043 | [1638, 1125, 826, 418] | True |
| 5 | 0.2627 | 13783.1 | 0.0988 | [1048, 947, 855, 761, 396] | True |
| 6 | 0.2585 | 13068.8 | 0.0562 | [1035, 979, 786, 700, 282, 225] | True |
| 7 | 0.2663 | 12117.1 | 0.0871 | [982, 734, 695, 500, 386, 361, 349] | True |
| 8 | 0.2774 | 11364.1 | 0.0344 | [915, 764, 730, 503, 483, 238, 236, 138] | True |

## Tamaño de cada cluster

| cluster_id | count | pct_juegos | arquetipo |
| --- | --- | --- | --- |
| 0 | 468 | 11.7 | Cluster 0 |
| 1 | 2628 | 65.6 | Cluster 1 |
| 2 | 911 | 22.7 | Cluster 2 |

## Centroides en unidades originales

| cluster_id | log_peak_players | months_observed | pct_time_to_peak | retention_ratio | trend_slope_yearly | volatility | log_peak_to_avg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 4.744 | 73.844 | 0.584 | 0.178 | 0.138 | 0.78 | 2.783 |
| 1 | 5.438 | 113.881 | 0.117 | 0.1 | -0.139 | 0.346 | 1.112 |
| 2 | 5.891 | 119.797 | 0.653 | 0.47 | 0.133 | 0.282 | 0.944 |

## Ficha técnica por arquetipo

| cluster_id | arquetipo | juegos | pct_juegos | mediana_pico_jugadores | mediana_meses_observados | mediana_pct_tiempo_al_pico | mediana_retencion | mediana_tendencia_anual_log | mediana_volatilidad | mediana_pico_sobre_promedio | pct_gratuitos | precio_medio | mediana_anio_lanzamiento | review_ratio_medio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Cluster 0 | 468 | 11.7 | 102 | 72 | 0.68 | 0.088 | 0.141 | 0.764 | 17.05 |  |  |  |  |
| 1 | Cluster 1 | 2628 | 65.6 | 170 | 113 | 0.05 | 0.071 | -0.12 | 0.333 | 2.95 |  |  |  |  |
| 2 | Cluster 2 | 911 | 22.7 | 260 | 118 | 0.66 | 0.454 | 0.097 | 0.258 | 2.44 |  |  |  |  |

## Porcentaje de juegos de cada cluster por género (top 8)

| arquetipo |
| --- |

## Juegos de ejemplo por cluster (top 5 por pico)

| cluster_id | rank_in_cluster | app_id | name | pico_jugadores | meses | retencion | release_year |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 671860 | BattleBit Remastered | 45198 | 36 | 0.012 |  |
| 0 | 2 | 323190 | Frostpunk | 19478 | 97 | 0.088 |  |
| 0 | 3 | 668580 | Atomic Heart | 18457 | 33 | 0.035 |  |
| 0 | 4 | 351940 | The Descendant | 10282 | 115 | 0.001 |  |
| 0 | 5 | 343710 | Kholat | 5044 | 123 | 0.001 |  |
| 1 | 1 | 578080 | PUBG: BATTLEGROUNDS | 1.58489e+06 | 102 | 0.184 |  |
| 1 | 2 | 553850 | HELLDIVERS™ 2 | 217046 | 19 | 0.225 |  |
| 1 | 3 | 261550 | Mount & Blade II: Bannerlord | 113493 | 66 | 0.185 |  |
| 1 | 4 | 582010 | Monster Hunter: World | 113236 | 85 | 0.09 |  |
| 1 | 5 | 779340 | Total War: THREE KINGDOMS | 102719 | 77 | 0.041 |  |
| 2 | 1 | 730 | Counter-Strike 2 | 1.11752e+06 | 158 | 0.828 |  |
| 2 | 2 | 271590 | Grand Theft Auto V Legacy | 145070 | 125 | 0.444 |  |
| 2 | 3 | 252490 | Rust | 142117 | 141 | 0.682 |  |
| 2 | 4 | 105600 | Terraria | 129809 | 158 | 0.193 |  |
| 2 | 5 | 413150 | Stardew Valley | 120134 | 117 | 0.606 |  |

## Curva típica: % del pico en meses seleccionados

| arquetipo | -12 | -6 | 0 | 6 | 12 | 24 | 36 | 60 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cluster 0 | 3.6 | 4.3 | 100 | 5.5 | 2.9 | 3.7 | 2.6 | 4.1 |
| Cluster 1 | 19.3 | 20 | 100 | 25.8 | 22.8 | 17.6 | 14 | 10.3 |
| Cluster 2 | 42.2 | 44.6 | 100 | 51.5 | 53.6 | 49.1 | 44.5 | 44 |

## Exposición en Twitch por arquetipo (juegos dentro de la ventana 2016-01 a 2024-09)

| cluster_id | arquetipo | juegos_en_ventana | pct_alguna_vez_top200 | meses_top200_promedio | mediana_horas_vistas_si_aparece | mejor_rank |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | Cluster 0 | 468 | 2.6 | 0.05 | 883459 | 29 |
| 1 | Cluster 1 | 2628 | 13.5 | 0.77 | 920871 | 5 |
| 2 | Cluster 2 | 911 | 19.2 | 3.66 | 2264212 | 2 |
