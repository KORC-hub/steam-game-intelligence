# Resultados del diagn?stico ? 03_diagnostico_steamcharts_history

- **Notebook:** `03_diagnostico_steamcharts_history`
- **Ejecutado:** `2026-10-18T22:15:24.839141+00:00` (zona horaria del driver)
- **Estado:** `completed`
- **Objetivo:** conservar los resultados efectivos de las validaciones SQL del notebook para su revisi?n local.

## Tablas inspeccionadas
- `steam_game_intelligence.bronze.steamcharts_2025_history_data`

## Consultas y resultados

### Consulta de celda SQL 1
_Filas exportadas: 1; m?ximo aplicado: 200._

| total_rows | distinct_app_ids | distinct_month_strings | min_month_string | max_month_string | first_ingested_at | last_ingested_at |
| --- | --- | --- | --- | --- | --- | --- |
| 612265 | 6729 | 159 | Apr-13 | Sep-25 | 2026-09-16 18:46:47.007169 | 2026-09-16 18:46:47.007169 |

### Consulta de celda SQL 2
_Filas exportadas: 0; m?ximo aplicado: 200._

No se detectaron registros que incumplan esta validaci?n o la consulta no devolvi? filas.

### Consulta de celda SQL 3
_Filas exportadas: 159; m?ximo aplicado: 200._

| month | parsed_month | row_count |
| --- | --- | --- |
| Apr-13 | NULL | 1118 |
| Apr-14 | NULL | 1515 |
| Apr-15 | NULL | 2247 |
| Apr-16 | NULL | 3318 |
| Apr-17 | NULL | 4513 |
| Apr-18 | NULL | 5562 |
| Apr-19 | NULL | 6029 |
| Apr-20 | NULL | 4946 |
| Apr-21 | NULL | 4709 |
| Apr-22 | NULL | 4561 |
| Apr-23 | NULL | 4481 |
| Apr-24 | NULL | 4102 |
| Apr-25 | NULL | 3859 |
| Aug-12 | NULL | 886 |
| Aug-13 | NULL | 1171 |
| Aug-14 | NULL | 1754 |
| Aug-15 | NULL | 2560 |
| Aug-16 | NULL | 3650 |
| Aug-17 | NULL | 4922 |
| Aug-18 | NULL | 5685 |
| Aug-19 | NULL | 6022 |
| Aug-20 | NULL | 5153 |
| Aug-21 | NULL | 4629 |
| Aug-22 | NULL | 4485 |
| Aug-23 | NULL | 4308 |
| Aug-24 | NULL | 4055 |
| Aug-25 | NULL | 3872 |
| Dec-12 | NULL | 1009 |
| Dec-13 | NULL | 1338 |
| Dec-14 | NULL | 1977 |
| Dec-15 | NULL | 2871 |
| Dec-16 | NULL | 4220 |
| Dec-17 | NULL | 5458 |
| Dec-18 | NULL | 5866 |
| Dec-19 | NULL | 5021 |
| Dec-20 | NULL | 4980 |
| Dec-21 | NULL | 4675 |
| Dec-22 | NULL | 4528 |
| Dec-23 | NULL | 4305 |
| Dec-24 | NULL | 4015 |
| Feb-13 | NULL | 1052 |
| Feb-14 | NULL | 1381 |
| Feb-15 | NULL | 2089 |
| Feb-16 | NULL | 3029 |
| Feb-17 | NULL | 4278 |
| Feb-18 | NULL | 5622 |
| Feb-19 | NULL | 5849 |
| Feb-20 | NULL | 4904 |
| Feb-21 | NULL | 4767 |
| Feb-22 | NULL | 4616 |
| Feb-23 | NULL | 4376 |
| Feb-24 | NULL | 4106 |
| Feb-25 | NULL | 3881 |
| Jan-13 | NULL | 1029 |
| Jan-14 | NULL | 1338 |
| Jan-15 | NULL | 2025 |
| Jan-16 | NULL | 2938 |
| Jan-17 | NULL | 4203 |
| Jan-18 | NULL | 5563 |
| Jan-19 | NULL | 5906 |
| Jan-20 | NULL | 4995 |
| Jan-21 | NULL | 4886 |
| Jan-22 | NULL | 4684 |
| Jan-23 | NULL | 4518 |
| Jan-24 | NULL | 4204 |
| Jan-25 | NULL | 3990 |
| Jul-12 | NULL | 860 |
| Jul-13 | NULL | 1149 |
| Jul-14 | NULL | 1696 |
| Jul-15 | NULL | 2468 |
| Jul-16 | NULL | 3531 |
| Jul-17 | NULL | 4824 |
| Jul-18 | NULL | 5705 |
| Jul-19 | NULL | 6006 |
| Jul-20 | NULL | 4961 |
| Jul-21 | NULL | 4726 |
| Jul-22 | NULL | 4636 |
| Jul-23 | NULL | 4344 |
| Jul-24 | NULL | 4085 |
| Jul-25 | NULL | 3933 |
| Jun-13 | NULL | 1138 |
| Jun-14 | NULL | 1638 |
| Jun-15 | NULL | 2410 |
| Jun-16 | NULL | 3441 |
| Jun-17 | NULL | 4708 |
| Jun-18 | NULL | 5648 |
| Jun-19 | NULL | 5973 |
| Jun-20 | NULL | 4864 |
| Jun-21 | NULL | 4714 |
| Jun-22 | NULL | 4596 |
| Jun-23 | NULL | 4338 |
| Jun-24 | NULL | 4067 |
| Jun-25 | NULL | 3833 |
| Mar-13 | NULL | 1098 |
| Mar-14 | NULL | 1435 |
| Mar-15 | NULL | 2173 |
| Mar-16 | NULL | 3140 |
| Mar-17 | NULL | 4412 |
| Mar-18 | NULL | 5693 |
| Mar-19 | NULL | 5911 |
| Mar-20 | NULL | 4985 |
| Mar-21 | NULL | 4814 |
| Mar-22 | NULL | 4565 |
| Mar-23 | NULL | 4469 |
| Mar-24 | NULL | 4132 |
| Mar-25 | NULL | 3917 |
| May-13 | NULL | 1128 |
| May-14 | NULL | 1581 |
| May-15 | NULL | 2337 |
| May-16 | NULL | 3331 |
| May-17 | NULL | 4601 |
| May-18 | NULL | 5630 |
| May-19 | NULL | 5936 |
| May-20 | NULL | 4962 |
| May-21 | NULL | 4781 |
| May-22 | NULL | 4583 |
| May-23 | NULL | 4439 |
| May-24 | NULL | 4143 |
| May-25 | NULL | 3921 |
| Nov-12 | NULL | 975 |
| Nov-13 | NULL | 1300 |
| Nov-14 | NULL | 1924 |
| Nov-15 | NULL | 2793 |
| Nov-16 | NULL | 3942 |
| Nov-17 | NULL | 5311 |
| Nov-18 | NULL | 5835 |
| Nov-19 | NULL | 4969 |
| Nov-20 | NULL | 5110 |
| Nov-21 | NULL | 4654 |
| Nov-22 | NULL | 4452 |
| Nov-23 | NULL | 4217 |
| Nov-24 | NULL | 3932 |
| Oct-12 | NULL | 946 |
| Oct-13 | NULL | 1255 |
| Oct-14 | NULL | 1857 |
| Oct-15 | NULL | 2725 |
| Oct-16 | NULL | 3841 |
| Oct-17 | NULL | 5206 |
| Oct-18 | NULL | 5789 |
| Oct-19 | NULL | 4914 |
| Oct-20 | NULL | 5149 |
| Oct-21 | NULL | 4599 |
| Oct-22 | NULL | 4457 |
| Oct-23 | NULL | 4207 |
| Oct-24 | NULL | 3995 |
| Sep-12 | NULL | 911 |
| Sep-13 | NULL | 1204 |
| Sep-14 | NULL | 1796 |
| Sep-15 | NULL | 2631 |
| Sep-16 | NULL | 3737 |
| Sep-17 | NULL | 5034 |
| Sep-18 | NULL | 5712 |
| Sep-19 | NULL | 5692 |
| Sep-20 | NULL | 5118 |
| Sep-21 | NULL | 4527 |
| Sep-22 | NULL | 4449 |
| Sep-23 | NULL | 4179 |
| Sep-24 | NULL | 4031 |
| Sep-25 | NULL | 3877 |

### Consulta de celda SQL 4
_Filas exportadas: 1; m?ximo aplicado: 200._

| unparsed_month_rows | blank_month_rows | invalid_appid_rows | negative_avg_players_rows | negative_peak_players_rows | gain_percent_below_minus_100_rows | missing_ingestion_timestamp |
| --- | --- | --- | --- | --- | --- | --- |
| 612265 | 0 | 0 | 0 | 0 | 0 | 0 |

### Consulta de celda SQL 5
_Filas exportadas: 0; m?ximo aplicado: 200._

No se detectaron registros que incumplan esta validaci?n o la consulta no devolvi? filas.

### Consulta de celda SQL 6
_Filas exportadas: 0; m?ximo aplicado: 200._

No se detectaron registros que incumplan esta validaci?n o la consulta no devolvi? filas.

### Consulta de celda SQL 7
_Filas exportadas: 200; m?ximo aplicado: 200._

| month | avg_players | gain | gain_percent | peak_players | name | steam_appid | _ingested_at | _source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sep-25 | 7805.25 | 883.12 | 0.1276 | 13254 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Aug-25 | 6922.13 | -449.35 | -0.061 | 12168 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jul-25 | 7371.48 | -833.5 | -0.1016 | 13951 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jun-25 | 8204.98 | -847.53 | -0.09359999999999999 | 15798 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| May-25 | 9052.51 | -471.31 | -0.0495 | 15333 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Apr-25 | 9523.82 | -849.53 | -0.0819 | 17727 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Mar-25 | 10373.35 | -1190.16 | -0.10289999999999999 | 18180 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Feb-25 | 11563.5 | -341.15 | -0.0287 | 18934 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jan-25 | 11904.66 | 413.55 | 0.036000000000000004 | 20626 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Dec-24 | 11491.11 | 1253.53 | 0.12240000000000001 | 19006 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Nov-24 | 10237.58 | 310.83 | 0.0313 | 17065 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Oct-24 | 9926.75 | 645.11 | 0.0695 | 16821 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Sep-24 | 9281.64 | 407.25 | 0.045899999999999996 | 16410 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Aug-24 | 8874.39 | -1609.88 | -0.1536 | 14878 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jul-24 | 10484.26 | 820.42 | 0.0849 | 18909 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jun-24 | 9663.84 | 692.22 | 0.07719999999999999 | 15671 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| May-24 | 8971.63 | 746.44 | 0.0908 | 15664 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Apr-24 | 8225.19 | -645.74 | -0.0728 | 14470 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Mar-24 | 8870.93 | 687.48 | 0.084 | 15954 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Feb-24 | 8183.44 | -413.77 | -0.0481 | 14925 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jan-24 | 8597.22 | 404.76 | 0.049400000000000006 | 15597 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Dec-23 | 8192.45 | 216.76 | 0.027200000000000002 | 14596 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Nov-23 | 7975.7 | -26.73 | -0.0033 | 14415 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Oct-23 | 8002.42 | 403.87 | 0.053200000000000004 | 14219 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Sep-23 | 7598.56 | 85.95 | 0.011399999999999999 | 13166 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Aug-23 | 7512.6 | -343.71 | -0.0437 | 12412 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jul-23 | 7856.31 | 193.59 | 0.0253 | 13232 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jun-23 | 7662.73 | -100.78 | -0.013000000000000001 | 13078 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| May-23 | 7763.5 | -695.43 | -0.08220000000000001 | 13587 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Apr-23 | 8458.93 | -444.41 | -0.0499 | 15526 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Mar-23 | 8903.35 | -363.64 | -0.0392 | 15828 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Feb-23 | 9266.99 | -497.47 | -0.0509 | 16364 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jan-23 | 9764.46 | 590.19 | 0.0643 | 17136 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Dec-22 | 9174.27 | 520.82 | 0.0602 | 16245 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Nov-22 | 8653.45 | 476.15 | 0.0582 | 15888 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Oct-22 | 8177.3 | 172.54 | 0.0216 | 13709 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Sep-22 | 8004.76 | -682.2 | -0.0785 | 13455 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Aug-22 | 8686.96 | -340.27 | -0.0377 | 13191 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jul-22 | 9027.23 | 444.17 | 0.051699999999999996 | 14019 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jun-22 | 8583.06 | -120.59 | -0.0139 | 13707 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| May-22 | 8703.65 | -874.61 | -0.0913 | 14189 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Apr-22 | 9578.26 | -196.28 | -0.020099999999999996 | 16636 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Mar-22 | 9774.55 | -782.56 | -0.0741 | 16745 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Feb-22 | 10557.11 | 204.87 | 0.019799999999999998 | 18714 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jan-22 | 10352.24 | 989.88 | 0.1057 | 18392 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Dec-21 | 9362.36 | 221.01 | 0.0242 | 16534 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Nov-21 | 9141.35 | 469.64 | 0.0542 | 16321 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Oct-21 | 8671.71 | 210.59 | 0.024900000000000002 | 15631 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Sep-21 | 8461.12 | -390.07 | -0.0441 | 14559 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Aug-21 | 8851.19 | -286.57 | -0.031400000000000004 | 14064 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jul-21 | 9137.76 | -359.69 | -0.0379 | 14972 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jun-21 | 9497.45 | -1243.5 | -0.1158 | 16391 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| May-21 | 10740.95 | -1685.32 | -0.1356 | 18089 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Apr-21 | 12426.28 | 114.93 | 0.009300000000000001 | 21562 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Mar-21 | 12311.34 | 220.02 | 0.0182 | 22140 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Feb-21 | 12091.33 | -1002.98 | -0.0766 | 21626 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jan-21 | 13094.31 | 854.78 | 0.0698 | 23762 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Dec-20 | 12239.53 | 960.83 | 0.0852 | 22645 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Nov-20 | 11278.7 | 958.12 | 0.0928 | 20908 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Oct-20 | 10320.58 | 336.63 | 0.0337 | 17908 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Sep-20 | 9983.94 | -680.97 | -0.0639 | 16041 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Aug-20 | 10664.91 | -867.54 | -0.07519999999999999 | 16485 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jul-20 | 11532.45 | -543.85 | -0.045 | 18159 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jun-20 | 12076.3 | -3271.2 | -0.21309999999999998 | 21446 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| May-20 | 15347.51 | -2417.08 | -0.1361 | 29589 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Apr-20 | 17764.58 | 5255.06 | 0.4201 | 31782 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Mar-20 | 12509.52 | 2835.54 | 0.29309999999999997 | 30500 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Feb-20 | 9673.98 | -523.56 | -0.0513 | 17705 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jan-20 | 10197.54 | 622.14 | 0.065 | 19141 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Dec-19 | 9575.4 | 801.58 | 0.09140000000000001 | 18196 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Nov-19 | 8773.82 | 490.26 | 0.0592 | 15994 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Oct-19 | 8283.56 | -179.98 | -0.0213 | 14937 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Sep-19 | 8463.54 | -696.38 | -0.076 | 14661 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Aug-19 | 9159.92 | -157.5 | -0.0169 | 14902 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jul-19 | 9317.42 | 151.81 | 0.0166 | 15309 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jun-19 | 9165.61 | -80.97 | -0.0088 | 14925 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| May-19 | 9246.58 | -317.98 | -0.0332 | 16503 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Apr-19 | 9564.55 | -962.04 | -0.09140000000000001 | 17373 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Mar-19 | 10526.59 | -1227.21 | -0.10439999999999999 | 19302 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Feb-19 | 11753.8 | -864.14 | -0.06849999999999999 | 21432 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jan-19 | 12617.94 | 1034.28 | 0.08929999999999999 | 22902 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Dec-18 | 11583.65 | 1211.48 | 0.1168 | 21858 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Nov-18 | 10372.17 | 624.92 | 0.0641 | 20591 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Oct-18 | 9747.26 | -10.04 | -0.001 | 18183 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Sep-18 | 9757.29 | -683.95 | -0.0655 | 17531 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Aug-18 | 10441.25 | -684.15 | -0.061500000000000006 | 17093 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jul-18 | 11125.39 | 177.45 | 0.016200000000000003 | 18703 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jun-18 | 10947.94 | 115.97 | 0.010700000000000001 | 18604 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| May-18 | 10831.97 | -934.32 | -0.0794 | 18895 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Apr-18 | 11766.29 | -2257.31 | -0.161 | 22637 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Mar-18 | 14023.6 | -594.31 | -0.0407 | 25812 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Feb-18 | 14617.92 | -501.99 | -0.0332 | 26135 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jan-18 | 15119.9 | 1383 | 0.1007 | 27589 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Dec-17 | 13736.9 | 1686.41 | 0.1399 | 25689 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Nov-17 | 12050.49 | 977.92 | 0.0883 | 24734 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Oct-17 | 11072.57 | 353.59 | 0.033 | 20764 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Sep-17 | 10718.98 | -630.87 | -0.0556 | 18685 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Aug-17 | 11349.85 | -378.43 | -0.0323 | 18292 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jul-17 | 11728.28 | -419.12 | -0.0345 | 20303 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jun-17 | 12147.4 | 28.52 | 0.0024 | 20229 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| May-17 | 12118.87 | -939.24 | -0.0719 | 21838 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Apr-17 | 13058.12 | -1253.16 | -0.0876 | 22842 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Mar-17 | 14311.28 | -1314.58 | -0.08410000000000001 | 26577 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Feb-17 | 15625.86 | -455.31 | -0.028300000000000002 | 28071 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jan-17 | 16081.17 | 1864.74 | 0.13119999999999998 | 29300 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Dec-16 | 14216.43 | 768.26 | 0.0571 | 26909 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Nov-16 | 13448.17 | 445.52 | 0.034300000000000004 | 24792 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Oct-16 | 13002.65 | 418.17 | 0.0332 | 23413 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Sep-16 | 12584.48 | -562.96 | -0.042800000000000005 | 21984 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Aug-16 | 13147.45 | 34.78 | 0.0027 | 21491 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jul-16 | 13112.67 | -170.04 | -0.0128 | 21136 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jun-16 | 13282.71 | 212.82 | 0.0163 | 22585 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| May-16 | 13069.89 | -597.82 | -0.0437 | 22998 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Apr-16 | 13667.71 | -1761.1 | -0.11410000000000001 | 24994 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Mar-16 | 15428.81 | -967.82 | -0.059000000000000004 | 28136 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Feb-16 | 16396.64 | -246.65 | -0.0148 | 29617 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jan-16 | 16643.29 | 1988.07 | 0.13570000000000002 | 29670 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Dec-15 | 14655.22 | 810.51 | 0.058499999999999996 | 27926 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Nov-15 | 13844.71 | 615.83 | 0.0466 | 26133 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Oct-15 | 13228.88 | 342.42 | 0.026600000000000002 | 24278 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Sep-15 | 12886.46 | -1098.97 | -0.0786 | 23130 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Aug-15 | 13985.42 | -416.88 | -0.028900000000000002 | 22650 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jul-15 | 14402.31 | 152.28 | 0.010700000000000001 | 23624 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jun-15 | 14250.03 | -74.15 | -0.0052 | 24177 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| May-15 | 14324.18 | -1413.44 | -0.0898 | 26466 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Apr-15 | 15737.62 | -1702.04 | -0.09759999999999999 | 30333 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Mar-15 | 17439.66 | -1361.65 | -0.0724 | 33107 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Feb-15 | 18801.32 | -965.94 | -0.0489 | 34453 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jan-15 | 19767.26 | 989.08 | 0.0527 | 37018 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Dec-14 | 18778.18 | 1485.7 | 0.0859 | 36393 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Nov-14 | 17292.48 | 656.01 | 0.0394 | 33495 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Oct-14 | 16636.47 | 307.96 | 0.0189 | 31690 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Sep-14 | 16328.5 | -1694.35 | -0.094 | 30379 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Aug-14 | 18022.85 | -91.66 | -0.0051 | 29564 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jul-14 | 18114.51 | 123.15 | 0.0068000000000000005 | 30469 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jun-14 | 17991.36 | 525.83 | 0.0301 | 31392 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| May-14 | 17465.53 | -1290.67 | -0.0688 | 33755 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Apr-14 | 18756.2 | -1728.85 | -0.08439999999999999 | 35774 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Mar-14 | 20485.05 | -1722.63 | -0.0776 | 39230 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Feb-14 | 22207.68 | -1114.3 | -0.0478 | 41945 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jan-14 | 23321.98 | 1900.11 | 0.08869999999999999 | 44491 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Dec-13 | 21421.87 | 1719.46 | 0.0873 | 40743 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Nov-13 | 19702.41 | 621.56 | 0.0326 | 39826 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Oct-13 | 19080.85 | -106.94 | -0.005600000000000001 | 36655 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Sep-13 | 19187.79 | -2109.73 | -0.09910000000000001 | 36983 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Aug-13 | 21297.53 | 816.1 | 0.0398 | 34230 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jul-13 | 20481.43 | 336.54 | 0.0167 | 34412 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jun-13 | 20144.89 | 244.08 | 0.0123 | 35960 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| May-13 | 19900.81 | -1303.65 | -0.061500000000000006 | 36913 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Apr-13 | 21204.46 | -2934.69 | -0.1216 | 43856 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Mar-13 | 24139.15 | -4239.27 | -0.1494 | 49412 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Feb-13 | 28378.42 | -6436.05 | -0.18489999999999998 | 60134 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jan-13 | 34814.47 | 2818.4 | 0.08810000000000001 | 65188 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Dec-12 | 31996.07 | 2326.1 | 0.0784 | 61189 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Nov-12 | 29669.97 | 833.67 | 0.028900000000000002 | 56957 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Oct-12 | 28836.29 | -596.27 | -0.0203 | 56053 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Sep-12 | 29432.56 | -3663.24 | -0.1107 | 55321 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Aug-12 | 33095.8 | -1043.4 | -0.030600000000000002 | 53685 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jul-12 | 34139.2 | - | 0.0 | 53967 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Sep-25 | 48.17 | -1.97 | -0.0392 | 115 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Aug-25 | 50.14 | -2.39 | -0.0454 | 126 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jul-25 | 52.53 | 0.95 | 0.0184 | 113 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jun-25 | 51.58 | 1.89 | 0.038 | 109 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| May-25 | 49.69 | -1.95 | -0.0378 | 108 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Apr-25 | 51.64 | -0.98 | -0.018600000000000002 | 116 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Mar-25 | 52.61 | -2.17 | -0.039599999999999996 | 116 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Feb-25 | 54.79 | -4.11 | -0.0698 | 127 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jan-25 | 58.9 | 2.69 | 0.0479 | 131 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Dec-24 | 56.2 | -0.75 | -0.0132 | 109 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Nov-24 | 56.95 | 4.57 | 0.0873 | 121 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Oct-24 | 52.38 | -1.39 | -0.0258 | 102 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Sep-24 | 53.77 | -3.33 | -0.0583 | 114 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Aug-24 | 57.1 | -2.92 | -0.048600000000000004 | 106 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jul-24 | 60.01 | 0.86 | 0.014499999999999999 | 106 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jun-24 | 59.16 | 5.46 | 0.1017 | 113 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| May-24 | 53.7 | 0.41 | 0.0077 | 110 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Apr-24 | 53.29 | -4.19 | -0.0729 | 110 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Mar-24 | 57.48 | -5.84 | -0.0922 | 127 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Feb-24 | 63.32 | -6.42 | -0.092 | 137 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jan-24 | 69.73 | 5.37 | 0.0834 | 138 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Dec-23 | 64.36 | 0.64 | 0.0101 | 125 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Nov-23 | 63.72 | 6.84 | 0.1202 | 145 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Oct-23 | 56.89 | -6.59 | -0.1038 | 105 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Sep-23 | 63.48 | 0.34 | 0.0054 | 126 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Aug-23 | 63.14 | -5.85 | -0.0848 | 123 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jul-23 | 68.99 | 14.11 | 0.2572 | 143 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jun-23 | 54.88 | -7.59 | -0.1215 | 110 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| May-23 | 62.47 | -4.44 | -0.0663 | 126 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Apr-23 | 66.9 | -3.05 | -0.0435 | 134 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Mar-23 | 69.95 | 10.31 | 0.17300000000000001 | 139 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Feb-23 | 59.63 | -6.41 | -0.0971 | 123 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jan-23 | 66.05 | 3.85 | 0.061799999999999994 | 143 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Dec-22 | 62.2 | 4.65 | 0.0808 | 136 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Nov-22 | 57.55 | 6.43 | 0.1257 | 130 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Oct-22 | 51.12 | 1.79 | 0.0362 | 108 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Sep-22 | 49.34 | -5.73 | -0.1041 | 113 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Aug-22 | 55.07 | -6.33 | -0.10300000000000001 | 118 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jul-22 | 61.4 | 3.01 | 0.0516 | 122 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| Jun-22 | 58.38 | 4.65 | 0.08650000000000001 | 125 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |
| May-22 | 53.73 | -4.17 | -0.07200000000000001 | 113 | Team Fortress Classic | 20 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |

### Muestra de estructura (una fila)
_Filas exportadas: 1; m?ximo aplicado: 200._

| month | avg_players | gain | gain_percent | peak_players | name | steam_appid | _ingested_at | _source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sep-25 | 7805.25 | 883.12 | 0.1276 | 13254 | Counter-Strike | 10 | 2026-09-16 18:46:47.007169 | https://www.kaggle.com/datasets/lunthu/steam-monthly-average-players |

## Hallazgos y conclusiones
Los hallazgos deben interpretarse a partir de los conteos y muestras exportados; esta celda no inventa conclusiones ni marca como aprobada una validaci?n no ejecutada.
