# Resultados del diagn?stico ? 04_diagnostico_twitch_top200

- **Notebook:** `04_diagnostico_twitch_top200`
- **Ejecutado:** `2026-10-18T22:16:00.287339+00:00` (zona horaria del driver)
- **Estado:** `completed`
- **Objetivo:** conservar los resultados efectivos de las validaciones SQL del notebook para su revisi?n local.

## Tablas inspeccionadas
- `steam_game_intelligence.bronze.twitch_top_200_games_data`

## Consultas y resultados

### Consulta de celda SQL 1
_Filas exportadas: 1; m?ximo aplicado: 200._

| total_rows | distinct_games | distinct_years | min_year | max_year | min_month | max_month | first_ingested_at | last_ingested_at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 21000 | 2359 | 9 | 2016 | 2024 | 1 | 12 | 2026-09-16 18:47:15.962265 | 2026-09-16 18:47:15.962265 |

### Consulta de celda SQL 2
_Filas exportadas: 1; m?ximo aplicado: 200._

| column_name | null_count |
| --- | --- |
| Game | 1 |

### Consulta de celda SQL 3
_Filas exportadas: 1; m?ximo aplicado: 200._

| year_outside_expected_range | invalid_month | invalid_rank | rank_above_top200 | blank_game | missing_ingestion_timestamp |
| --- | --- | --- | --- | --- | --- |
| 1800 | 0 | 0 | 0 | 0 | 0 |

### Consulta de celda SQL 4
_Filas exportadas: 0; m?ximo aplicado: 200._

No se detectaron registros que incumplan esta validaci?n o la consulta no devolvi? filas.

### Consulta de celda SQL 5
_Filas exportadas: 11; m?ximo aplicado: 200._

| Year | Month | normalized_game | row_count | distinct_ranks | best_rank | worst_rank |
| --- | --- | --- | --- | --- | --- | --- |
| 2023 | 3 | resident evil 4 | 2 | 2 | 11 | 80 |
| 2021 | 9 | retro | 2 | 2 | 72 | 120 |
| 2021 | 10 | retro | 2 | 2 | 83 | 103 |
| 2023 | 1 | among us | 2 | 2 | 68 | 156 |
| 2018 | 9 | dungeons & dragons | 2 | 2 | 75 | 103 |
| 2020 | 11 | who wants to be a millionaire | 2 | 2 | 136 | 158 |
| 2016 | 10 | resident evil | 2 | 2 | 116 | 180 |
| 2019 | 1 | atlas | 2 | 2 | 15 | 50 |
| 2019 | 1 | resident evil 2 | 2 | 2 | 13 | 130 |
| 2022 | 7 | stray | 2 | 2 | 27 | 153 |
| 2024 | 5 | paper mario: the thousand-year door | 2 | 2 | 136 | 197 |

### Consulta de celda SQL 6
_Filas exportadas: 1; m?ximo aplicado: 200._

| negative_hours_watched | negative_hours_streamed | negative_peak_viewers | negative_peak_channels | negative_streamers | negative_avg_viewers | negative_avg_channels | negative_avg_viewer_ratio |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

### Consulta de celda SQL 7
_Filas exportadas: 200; m?ximo aplicado: 200._

| Rank | Game | Month | Year | Hours_watched | Hours_streamed | Peak_viewers | Peak_channels | Streamers | Avg_viewers | Avg_channels | Avg_viewer_ratio | _ingested_at | _source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 162 | NULL | 2 | 2019 | 317951 | 77004 | 30919 | 5804 | 21758 | 473 | 114 | 4.13 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 1 | Just Chatting | 1 | 2024 | 273155353 | 3479321 | 812918 | 6983 | 514218 | 367638 | 4682 | 78.51 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 2 | Grand Theft Auto V | 1 | 2024 | 180310854 | 2500049 | 617783 | 5829 | 271064 | 242679 | 3364 | 72.12 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 3 | League of Legends | 1 | 2024 | 143008800 | 2508016 | 782121 | 6395 | 224380 | 192474 | 3375 | 57.02 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 4 | Escape from Tarkov | 1 | 2024 | 82110906 | 1194696 | 393116 | 2755 | 56431 | 110512 | 1607 | 68.73 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 5 | Fortnite | 1 | 2024 | 72330309 | 8256190 | 503325 | 23219 | 1498156 | 97349 | 11111 | 8.76 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 6 | Palworld | 1 | 2024 | 60000529 | 2173736 | 434200 | 11031 | 231061 | 80754 | 2925 | 27.6 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 7 | VALORANT | 1 | 2024 | 59453011 | 3381408 | 182952 | 7060 | 342692 | 80017 | 4551 | 17.58 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 8 | Counter-Strike | 1 | 2024 | 51869838 | 940786 | 301259 | 2538 | 134995 | 69811 | 1266 | 55.13 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 9 | Minecraft | 1 | 2024 | 45840958 | 1636640 | 651220 | 4136 | 302688 | 61697 | 2202 | 28.01 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 10 | Dota 2 | 1 | 2024 | 43258831 | 910263 | 190051 | 2380 | 68280 | 58221 | 1225 | 47.52 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 11 | Call of Duty: Warzone | 1 | 2024 | 42261560 | 3042426 | 157556 | 7910 | 345652 | 56879 | 4094 | 13.89 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 12 | EA Sports FC 24 | 1 | 2024 | 38082533 | 986925 | 595991 | 4718 | 187220 | 51255 | 1328 | 38.59 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 13 | World of Warcraft | 1 | 2024 | 23318426 | 882829 | 65973 | 2933 | 54843 | 31384 | 1188 | 26.41 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 14 | Apex Legends | 1 | 2024 | 23001527 | 1962586 | 125945 | 3959 | 218190 | 30957 | 2641 | 11.72 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 15 | Teamfight Tactics | 1 | 2024 | 18644812 | 235763 | 66540 | 518 | 32506 | 25093 | 317 | 79.08 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 16 | Lethal Company | 1 | 2024 | 16807111 | 865553 | 101492 | 3816 | 179422 | 22620 | 1164 | 19.42 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 17 | Dead by Daylight | 1 | 2024 | 16629058 | 1080495 | 73342 | 2782 | 100672 | 22380 | 1454 | 15.39 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 18 | Rust | 1 | 2024 | 16149101 | 313196 | 125524 | 1229 | 34626 | 21734 | 421 | 51.56 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 19 | Slots | 1 | 2024 | 15024773 | 75953 | 58348 | 189 | 5332 | 20221 | 102 | 197.82 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 20 | Call of Duty: Modern Warfare III | 1 | 2024 | 14082221 | 1288104 | 113205 | 4396 | 117497 | 18953 | 1733 | 10.93 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 21 | Music | 1 | 2024 | 14035364 | 618578 | 68236 | 1629 | 52295 | 18890 | 832 | 22.69 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 22 | Tom Clancy's Rainbow Six Siege | 1 | 2024 | 13943000 | 1214945 | 250860 | 3564 | 247741 | 18765 | 1635 | 11.48 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 23 | Sports | 1 | 2024 | 13550210 | 105583 | 204258 | 412 | 12444 | 18237 | 142 | 128.34 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 24 | Overwatch 2 | 1 | 2024 | 12718735 | 1039863 | 31954 | 2367 | 147949 | 17118 | 1399 | 12.23 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 25 | Casino Jackpot | 1 | 2024 | 12290911 | 42706 | 72880 | 175 | 2666 | 16542 | 57 | 287.8 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 26 | Special Events | 1 | 2024 | 11378877 | 49854 | 744794 | 2798 | 9058 | 15314 | 67 | 228.24 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 27 | Virtual Casino | 1 | 2024 | 11275710 | 28682 | 37390 | 82 | 1259 | 15175 | 38 | 393.13 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 28 | PUBG: BATTLEGROUNDS | 1 | 2024 | 11179557 | 542007 | 181086 | 1338 | 54712 | 15046 | 729 | 20.63 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 29 | Path of Exile | 1 | 2024 | 11139554 | 184839 | 52592 | 485 | 9590 | 14992 | 248 | 60.27 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 30 | Street Fighter 6 | 1 | 2024 | 10985788 | 135475 | 136454 | 403 | 17353 | 14785 | 182 | 81.09 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 31 | Hearthstone | 1 | 2024 | 10899914 | 101802 | 31333 | 243 | 9651 | 14670 | 137 | 107.07 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 32 | Casino | 1 | 2024 | 9863134 | 24160 | 69704 | 128 | 1398 | 13274 | 32 | 408.24 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 33 | Monster Hunter: World | 1 | 2024 | 9645724 | 362241 | 72266 | 903 | 32208 | 12982 | 487 | 26.63 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 34 | ASMR | 1 | 2024 | 9518559 | 136191 | 21842 | 251 | 4228 | 12810 | 183 | 69.89 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 35 | Enshrouded | 1 | 2024 | 8754776 | 158648 | 221930 | 1827 | 19637 | 11783 | 213 | 55.18 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 36 | Art | 1 | 2024 | 8117785 | 500211 | 19224 | 1035 | 51924 | 10925 | 673 | 16.23 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 37 | Genshin Impact | 1 | 2024 | 7915720 | 675349 | 215097 | 4712 | 80366 | 10653 | 908 | 11.72 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 38 | Baldur's Gate 3 | 1 | 2024 | 6595870 | 561411 | 91906 | 1580 | 58083 | 8877 | 755 | 11.75 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 39 | TEKKEN 8 | 1 | 2024 | 6531889 | 139373 | 118728 | 2564 | 24242 | 8791 | 187 | 46.87 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 40 | ELDEN RING | 1 | 2024 | 6395762 | 444261 | 106131 | 1050 | 58937 | 8608 | 597 | 14.4 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 41 | Lost Ark | 1 | 2024 | 6286894 | 186394 | 33697 | 587 | 6879 | 8461 | 250 | 33.73 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 42 | I'm Only Sleeping | 1 | 2024 | 5742809 | 169501 | 70676 | 393 | 6919 | 7729 | 228 | 33.88 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 43 | Rocket League | 1 | 2024 | 5569250 | 646495 | 62996 | 1586 | 177240 | 7495 | 870 | 8.61 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 44 | Retro | 1 | 2024 | 5374341 | 200085 | 55237 | 397 | 12122 | 7233 | 269 | 26.86 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 45 | IRL | 1 | 2024 | 5351479 | 89638 | 41909 | 169 | 4275 | 7202 | 120 | 59.7 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 46 | World of Tanks | 1 | 2024 | 5343662 | 147466 | 44612 | 455 | 13347 | 7192 | 198 | 36.24 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 47 | Black Desert | 1 | 2024 | 5316183 | 155218 | 18298 | 335 | 8040 | 7155 | 208 | 34.25 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 48 | Dragon Ball | 1 | 2024 | 4861530 | 41565 | 17410 | 97 | 1182 | 6543 | 55 | 116.96 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 49 | Pools, Hot Tubs, and Beaches | 1 | 2024 | 4800909 | 63497 | 29041 | 123 | 3109 | 6461 | 85 | 75.61 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 50 | NBA 2K24 | 1 | 2024 | 4746671 | 783537 | 167107 | 2322 | 108557 | 6388 | 1054 | 6.06 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 51 | Albion Online | 1 | 2024 | 4659352 | 86796 | 13739 | 197 | 4651 | 6270 | 116 | 53.68 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 52 | Old School RuneScape | 1 | 2024 | 4542547 | 103672 | 43754 | 224 | 6339 | 6113 | 139 | 43.82 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 53 | THE FINALS | 1 | 2024 | 4541354 | 547004 | 22613 | 1718 | 125453 | 6112 | 736 | 8.3 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 54 | Destiny 2 | 1 | 2024 | 4445755 | 364530 | 16440 | 942 | 40700 | 5983 | 490 | 12.2 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 55 | DayZ | 1 | 2024 | 4396324 | 241450 | 64576 | 633 | 27753 | 5916 | 324 | 18.21 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 56 | Talk Shows & Podcasts | 1 | 2024 | 4351451 | 182562 | 63217 | 498 | 14078 | 5856 | 245 | 23.84 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 57 | Chess | 1 | 2024 | 4238479 | 49771 | 35083 | 154 | 8103 | 5704 | 66 | 85.16 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 58 | Madden NFL 24 | 1 | 2024 | 4182733 | 712337 | 166141 | 2651 | 133512 | 5629 | 958 | 5.87 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 59 | SMITE | 1 | 2024 | 4158775 | 154379 | 46515 | 423 | 17042 | 5597 | 207 | 26.94 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 60 | FINAL FANTASY XIV ONLINE | 1 | 2024 | 4122935 | 277057 | 98982 | 1112 | 22155 | 5549 | 372 | 14.88 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 61 | Like a Dragon: Infinite Wealth | 1 | 2024 | 3894366 | 92686 | 76403 | 875 | 6942 | 5241 | 124 | 42.02 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 62 | Sea of Thieves | 1 | 2024 | 3819422 | 226089 | 55555 | 763 | 31405 | 5140 | 304 | 16.89 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 63 | Pokémon Scarlet/Violet | 1 | 2024 | 3768597 | 172854 | 40977 | 683 | 16664 | 5072 | 232 | 21.8 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 64 | Diablo IV | 1 | 2024 | 3709422 | 184456 | 95787 | 2118 | 20804 | 4992 | 248 | 20.11 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 65 | MapleStory | 1 | 2024 | 3597858 | 90569 | 29342 | 303 | 4574 | 4842 | 121 | 39.73 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 66 | MapleStory Worlds | 1 | 2024 | 3530324 | 44784 | 51275 | 185 | 1752 | 4751 | 60 | 78.83 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 67 | Marvel Snap | 1 | 2024 | 3518561 | 33162 | 34890 | 150 | 3936 | 4735 | 44 | 106.1 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 68 | VRChat | 1 | 2024 | 3508270 | 81224 | 62903 | 592 | 11740 | 4721 | 109 | 43.19 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 69 | Red Dead Redemption 2 | 1 | 2024 | 3454780 | 344480 | 54495 | 883 | 52504 | 4649 | 463 | 10.03 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 70 | ROBLOX | 1 | 2024 | 3442961 | 690138 | 49582 | 1824 | 249428 | 4633 | 928 | 4.99 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 71 | Prince of Persia: The Lost Crown | 1 | 2024 | 3155308 | 59219 | 51830 | 395 | 9011 | 4246 | 79 | 53.28 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 72 | Anime World | 1 | 2024 | 3127848 | 83766 | 12076 | 211 | 3183 | 4209 | 112 | 37.34 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 73 | Call of Duty | 1 | 2024 | 3019717 | 2029735 | 9989 | 4887 | 279027 | 4064 | 2731 | 1.49 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 74 | Tibia | 1 | 2024 | 3017808 | 138929 | 9620 | 368 | 5407 | 4061 | 186 | 21.72 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 75 | Animals, Aquariums, and Zoos | 1 | 2024 | 3005018 | 171678 | 22099 | 281 | 1064 | 4044 | 231 | 17.5 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 76 | Age of Empires II | 1 | 2024 | 2996461 | 36743 | 31614 | 103 | 3737 | 4032 | 49 | 81.55 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 77 | Heroes of Might and Magic III: The Restoration of Erathia | 1 | 2024 | 2984751 | 26648 | 19822 | 81 | 1089 | 4017 | 35 | 112.01 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 78 | Poker | 1 | 2024 | 2939552 | 52175 | 18987 | 187 | 3910 | 3956 | 70 | 56.34 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 79 | Games + Demos | 1 | 2024 | 2915544 | 448852 | 77713 | 1477 | 114723 | 3924 | 604 | 6.5 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 80 | Honkai: Star Rail | 1 | 2024 | 2889443 | 146602 | 95697 | 801 | 23321 | 3888 | 197 | 19.71 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 81 | Hunt: Showdown 1896 | 1 | 2024 | 2879730 | 194480 | 10546 | 579 | 15145 | 3875 | 261 | 14.81 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 82 | Cult of the Lamb | 1 | 2024 | 2720041 | 101592 | 34536 | 822 | 16490 | 3660 | 136 | 26.77 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 83 | Always On | 1 | 2024 | 2691144 | 126760 | 5447 | 192 | 556 | 3621 | 170 | 21.23 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 84 | Software and Game Development | 1 | 2024 | 2646478 | 101215 | 17579 | 262 | 8896 | 3561 | 136 | 26.15 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 85 | Magic: The Gathering | 1 | 2024 | 2620934 | 50140 | 23766 | 129 | 5285 | 3527 | 67 | 52.27 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 86 | Poppy Playtime | 1 | 2024 | 2513983 | 19949 | 223983 | 857 | 7796 | 3383 | 26 | 126.02 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 87 | Among Us | 1 | 2024 | 2386087 | 65637 | 103364 | 250 | 29688 | 3211 | 88 | 36.35 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 88 | Ravendawn | 1 | 2024 | 2362523 | 42687 | 21621 | 344 | 2925 | 3179 | 57 | 55.35 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 89 | The Simpsons: Hit & Run | 1 | 2024 | 2311646 | 15929 | 6322 | 38 | 928 | 3111 | 21 | 145.12 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 90 | Rise Online | 1 | 2024 | 2299029 | 25927 | 38727 | 323 | 1346 | 3094 | 34 | 88.67 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 91 | Suicide Squad: Kill the Justice League | 1 | 2024 | 2240122 | 27558 | 154051 | 1105 | 6004 | 3014 | 37 | 81.29 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 92 | Crypto | 1 | 2024 | 2194606 | 53201 | 16828 | 119 | 1285 | 2953 | 71 | 41.25 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 93 | Super Smash Bros. Ultimate | 1 | 2024 | 2171392 | 65788 | 92750 | 248 | 8782 | 2922 | 88 | 33.01 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 94 | Poker Online: Texas Holdem | 1 | 2024 | 2077834 | 26002 | 19519 | 95 | 1707 | 2796 | 34 | 79.91 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 95 | Dark and Darker | 1 | 2024 | 2075044 | 72969 | 7826 | 202 | 4890 | 2792 | 98 | 28.44 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 96 | Fall Guys | 1 | 2024 | 2070006 | 130485 | 72282 | 361 | 52985 | 2786 | 175 | 15.86 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 97 | The Sims 4 | 1 | 2024 | 2059793 | 105189 | 14359 | 276 | 19556 | 2772 | 141 | 19.58 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 98 | StarCraft II | 1 | 2024 | 2004249 | 36419 | 11847 | 108 | 3014 | 2697 | 49 | 55.03 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 99 | DARK SOULS III | 1 | 2024 | 1966662 | 72566 | 36785 | 186 | 11518 | 2646 | 97 | 27.1 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 100 | iRacing | 1 | 2024 | 1937059 | 122442 | 31444 | 2270 | 8363 | 2607 | 164 | 15.82 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 101 | World of Warships | 1 | 2024 | 1919219 | 52966 | 14680 | 131 | 4068 | 2583 | 71 | 36.23 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 102 | New World: Aeternum | 1 | 2024 | 1889321 | 70643 | 5871 | 213 | 4917 | 2542 | 95 | 26.74 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 103 | Warframe | 1 | 2024 | 1874833 | 220664 | 83027 | 566 | 25121 | 2523 | 296 | 8.5 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 104 | 60 Seconds! Reatomized | 1 | 2024 | 1824170 | 8599 | 95127 | 39 | 3907 | 2455 | 11 | 212.14 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 105 | The Binding of Isaac: Repentance | 1 | 2024 | 1806095 | 42656 | 23000 | 117 | 7928 | 2430 | 57 | 42.34 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 106 | Phasmophobia | 1 | 2024 | 1704890 | 174386 | 14571 | 502 | 40216 | 2294 | 234 | 9.78 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 107 | Food & Drink | 1 | 2024 | 1621650 | 22606 | 32543 | 69 | 3621 | 2182 | 30 | 71.74 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 108 | The Last of Us Part II: Remastered | 1 | 2024 | 1598989 | 33718 | 54756 | 330 | 4713 | 2152 | 45 | 47.42 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 109 | Clash Royale | 1 | 2024 | 1586865 | 32409 | 10834 | 87 | 17224 | 2135 | 43 | 48.96 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 110 | Star Citizen | 1 | 2024 | 1546760 | 55995 | 9294 | 187 | 4036 | 2081 | 75 | 27.62 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 111 | Eco | 1 | 2024 | 1528035 | 16991 | 20281 | 64 | 893 | 2056 | 22 | 89.93 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 112 | Super Mario 64 | 1 | 2024 | 1525277 | 27740 | 97931 | 90 | 3182 | 2052 | 37 | 54.98 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 113 | Brotato | 1 | 2024 | 1486838 | 7266 | 18562 | 101 | 2950 | 2001 | 9 | 204.63 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 114 | Project Zomboid | 1 | 2024 | 1482181 | 86480 | 12088 | 215 | 11626 | 1994 | 116 | 17.14 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 115 | Lies of P | 1 | 2024 | 1402310 | 115006 | 91762 | 315 | 16379 | 1887 | 154 | 12.19 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 116 | The Legend of Zelda: Tears of the Kingdom | 1 | 2024 | 1401740 | 49993 | 91498 | 128 | 5429 | 1886 | 67 | 28.04 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 117 | Halo Infinite | 1 | 2024 | 1386025 | 110729 | 13674 | 500 | 20164 | 1865 | 149 | 12.52 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 118 | Trackmania | 1 | 2024 | 1357494 | 22434 | 13470 | 139 | 3681 | 1827 | 30 | 60.51 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 119 | Football Manager 2024 | 1 | 2024 | 1346620 | 32672 | 30866 | 129 | 2903 | 1812 | 43 | 41.22 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 120 | Mario Kart 8 Deluxe | 1 | 2024 | 1324825 | 45225 | 98064 | 268 | 9941 | 1783 | 60 | 29.29 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 121 | Lineage II | 1 | 2024 | 1312090 | 48076 | 3386 | 139 | 1897 | 1765 | 64 | 27.29 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 122 | Shiren the Wanderer: The Mystery Dungeon of Serpentcoil Island | 1 | 2024 | 1292516 | 7826 | 30676 | 137 | 558 | 1739 | 10 | 165.16 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 123 | BUCKSHOT ROULETTE | 1 | 2024 | 1273376 | 17601 | 74366 | 83 | 14227 | 1713 | 23 | 72.35 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 124 | Yu-Gi-Oh! Master Duel | 1 | 2024 | 1265756 | 58203 | 8706 | 152 | 10235 | 1703 | 78 | 21.75 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 125 | Euro Truck Simulator 2 | 1 | 2024 | 1244017 | 115045 | 21294 | 433 | 19978 | 1674 | 154 | 10.81 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 126 | Warcraft III | 1 | 2024 | 1226759 | 21449 | 23149 | 62 | 1582 | 1651 | 28 | 57.19 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 127 | Garena Free Fire | 1 | 2024 | 1225768 | 136521 | 27791 | 359 | 58310 | 1649 | 183 | 8.98 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 128 | Marbles on Stream | 1 | 2024 | 1222319 | 39294 | 30726 | 117 | 5525 | 1645 | 52 | 31.11 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 129 | Brawl Stars | 1 | 2024 | 1217523 | 89731 | 9903 | 256 | 42579 | 1638 | 120 | 13.57 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 130 | Cyberpunk 2077 | 1 | 2024 | 1201943 | 167226 | 10020 | 460 | 23607 | 1617 | 225 | 7.19 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 131 | Tekken 7 | 1 | 2024 | 1187168 | 37082 | 51759 | 175 | 6709 | 1597 | 49 | 32.01 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 132 | League of Legends: Wild Rift | 1 | 2024 | 1151970 | 73197 | 4778 | 171 | 14771 | 1550 | 98 | 15.74 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 133 | Party Animals | 1 | 2024 | 1130962 | 40373 | 53376 | 185 | 14646 | 1522 | 54 | 28.01 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 134 | The Elder Scrolls Online | 1 | 2024 | 1115279 | 82335 | 101666 | 257 | 8115 | 1501 | 110 | 13.55 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 135 | Stardew Valley | 1 | 2024 | 1111991 | 94380 | 12402 | 251 | 17446 | 1496 | 127 | 11.78 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 136 | SCUM | 1 | 2024 | 1104962 | 44190 | 10817 | 162 | 2788 | 1487 | 59 | 25.0 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 137 | Resident Evil 4 | 1 | 2024 | 1104956 | 100818 | 11835 | 253 | 18689 | 1487 | 135 | 10.96 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 138 | ARK: Survival Ascended | 1 | 2024 | 1091692 | 111434 | 8220 | 328 | 10764 | 1469 | 149 | 9.8 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 139 | Bloodborne | 1 | 2024 | 1088670 | 47287 | 16215 | 128 | 8229 | 1465 | 63 | 23.02 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 140 | The Legend of Zelda: Majora's Mask | 1 | 2024 | 1074783 | 11099 | 88655 | 36 | 1067 | 1446 | 14 | 96.84 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 141 | Eternal Return | 1 | 2024 | 1064162 | 34477 | 32144 | 116 | 2506 | 1432 | 46 | 30.87 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 142 | Pokémon UNITE | 1 | 2024 | 1056591 | 67798 | 7112 | 221 | 7291 | 1422 | 91 | 15.58 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 143 | War Thunder | 1 | 2024 | 1055228 | 140188 | 5161 | 372 | 23936 | 1420 | 188 | 7.53 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 144 | Ready or Not | 1 | 2024 | 1034328 | 42454 | 55862 | 157 | 13132 | 1392 | 57 | 24.36 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 145 | Farming Simulator 22 | 1 | 2024 | 1029044 | 102959 | 11361 | 326 | 15551 | 1384 | 138 | 9.99 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 146 | Yakuza 0 | 1 | 2024 | 1018240 | 19323 | 57480 | 59 | 2618 | 1370 | 26 | 52.7 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 147 | Hogwarts Legacy | 1 | 2024 | 1012425 | 159035 | 5329 | 491 | 26949 | 1362 | 214 | 6.37 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 148 | GODDESS OF VICTORY: NIKKE | 1 | 2024 | 1010918 | 20073 | 34333 | 86 | 2614 | 1360 | 27 | 50.36 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 149 | Throne and Liberty | 1 | 2024 | 997693 | 26977 | 27005 | 87 | 1048 | 1342 | 36 | 36.98 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 150 | Sekiro: Shadows Die Twice | 1 | 2024 | 988253 | 77007 | 13501 | 202 | 13192 | 1330 | 103 | 12.83 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 151 | The Legend of Zelda: Ocarina of Time | 1 | 2024 | 981467 | 37307 | 90948 | 129 | 3800 | 1320 | 50 | 26.31 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 152 | Metin2 | 1 | 2024 | 977620 | 25784 | 4879 | 99 | 2080 | 1315 | 34 | 37.92 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 153 | Makers & Crafting | 1 | 2024 | 976470 | 82871 | 3798 | 191 | 6831 | 1314 | 111 | 11.78 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 154 | Grand Theft Auto: San Andreas | 1 | 2024 | 970356 | 36647 | 14335 | 192 | 9633 | 1305 | 49 | 26.48 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 155 | Animal Crossing: New Horizons | 1 | 2024 | 970248 | 39218 | 8617 | 160 | 4208 | 1305 | 52 | 24.74 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 156 | osu! | 1 | 2024 | 921368 | 116280 | 8882 | 268 | 23247 | 1240 | 156 | 7.92 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 157 | Super Mario World | 1 | 2024 | 919216 | 18199 | 8644 | 61 | 1929 | 1237 | 24 | 50.51 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 158 | MIR 4 | 1 | 2024 | 898986 | 23524 | 5423 | 74 | 983 | 1209 | 31 | 38.22 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 159 | 7 Days to Die | 1 | 2024 | 888046 | 118177 | 20738 | 314 | 13231 | 1195 | 159 | 7.51 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 160 | Stream Raiders | 1 | 2024 | 883916 | 28694 | 18434 | 96 | 1069 | 1189 | 38 | 30.8 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 161 | Knight Online | 1 | 2024 | 879410 | 27590 | 7723 | 113 | 1381 | 1183 | 37 | 31.87 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 162 | Politics | 1 | 2024 | 876842 | 19312 | 20636 | 52 | 821 | 1180 | 25 | 45.4 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 163 | Mobile Legends: Bang Bang | 1 | 2024 | 874535 | 80380 | 7938 | 165 | 20469 | 1177 | 108 | 10.88 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 164 | PUBG Mobile | 1 | 2024 | 868926 | 83575 | 90491 | 225 | 30273 | 1169 | 112 | 10.4 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 165 | El Chavo | 1 | 2024 | 856944 | 9306 | 1818 | 19 | 111 | 1153 | 12 | 92.09 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 166 | Contraband Police | 1 | 2024 | 849727 | 7050 | 70190 | 29 | 2565 | 1143 | 9 | 120.53 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 167 | Escape from Tarkov: Arena | 1 | 2024 | 847693 | 96932 | 5776 | 374 | 11470 | 1140 | 130 | 8.75 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 168 | Yakuza Kiwami | 1 | 2024 | 845756 | 6613 | 53241 | 24 | 951 | 1138 | 8 | 127.89 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 169 | RimWorld | 1 | 2024 | 840514 | 29949 | 11667 | 88 | 2580 | 1131 | 40 | 28.06 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 170 | Dark Souls: Remastered | 1 | 2024 | 829629 | 55055 | 6873 | 153 | 8376 | 1116 | 74 | 15.07 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 171 | Granblue Fantasy Versus: Rising | 1 | 2024 | 821891 | 35171 | 13249 | 139 | 5158 | 1106 | 47 | 23.37 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 172 | Pummel Party | 1 | 2024 | 814240 | 10568 | 44505 | 84 | 4007 | 1095 | 14 | 77.05 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 173 | Mortal Kombat 1 | 1 | 2024 | 808726 | 75963 | 12067 | 242 | 19873 | 1088 | 102 | 10.65 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 174 | Pokémon Community Game | 1 | 2024 | 806477 | 47190 | 2690 | 110 | 1675 | 1085 | 63 | 17.09 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 175 | Valheim | 1 | 2024 | 792134 | 94322 | 3706 | 253 | 10215 | 1066 | 126 | 8.4 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 176 | FINAL FANTASY VII REMAKE | 1 | 2024 | 782937 | 65412 | 13312 | 173 | 7382 | 1053 | 88 | 11.97 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 177 | Heroes of the Storm | 1 | 2024 | 779313 | 35129 | 21418 | 93 | 2649 | 1048 | 47 | 22.18 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 178 | The Texas Chain Saw Massacre | 1 | 2024 | 774735 | 71968 | 10881 | 209 | 12602 | 1042 | 96 | 10.76 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 179 | Pokémon Trading Card Game | 1 | 2024 | 768484 | 23415 | 14610 | 106 | 2810 | 1034 | 31 | 32.82 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 180 | Raft | 1 | 2024 | 766989 | 34010 | 33752 | 118 | 7345 | 1032 | 45 | 22.55 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 181 | F1 23 | 1 | 2024 | 757551 | 101702 | 9402 | 1044 | 20402 | 1019 | 136 | 7.45 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 182 | Super Mario Maker 2 | 1 | 2024 | 743614 | 13880 | 95957 | 43 | 1304 | 1000 | 18 | 53.57 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 183 | Age of Empires IV | 1 | 2024 | 735947 | 23041 | 6919 | 67 | 2687 | 990 | 31 | 31.94 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 184 | Terraria | 1 | 2024 | 725665 | 85348 | 7310 | 200 | 16650 | 976 | 114 | 8.5 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 185 | Dungeons & Dragons | 1 | 2024 | 723391 | 51868 | 21713 | 282 | 5983 | 973 | 69 | 13.95 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 186 | God of War Ragnarök | 1 | 2024 | 723388 | 135533 | 15422 | 451 | 24017 | 973 | 182 | 5.34 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 187 | Jackbox Party Packs | 1 | 2024 | 719678 | 25321 | 14632 | 272 | 6135 | 968 | 34 | 28.42 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 188 | Sid Meier's Civilization VI | 1 | 2024 | 715466 | 23248 | 9646 | 67 | 2919 | 962 | 31 | 30.78 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 189 | Microsoft Flight Simulator | 1 | 2024 | 708236 | 53205 | 8731 | 151 | 6845 | 953 | 71 | 13.31 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 190 | Slay the Spire | 1 | 2024 | 686499 | 16321 | 8422 | 49 | 3063 | 923 | 21 | 42.06 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 191 | Diablo III | 1 | 2024 | 679397 | 33537 | 15836 | 338 | 3055 | 914 | 45 | 20.26 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 192 | Cuphead | 1 | 2024 | 677920 | 23668 | 64440 | 88 | 10298 | 912 | 31 | 28.64 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 193 | Epic Seven | 1 | 2024 | 665771 | 8026 | 7244 | 43 | 625 | 896 | 10 | 82.95 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 194 | Call of Duty: Mobile | 1 | 2024 | 652369 | 135738 | 11546 | 364 | 48020 | 878 | 182 | 4.81 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 195 | Hollow Knight | 1 | 2024 | 648729 | 67019 | 9366 | 174 | 13153 | 873 | 90 | 9.68 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 196 | Garry's Mod | 1 | 2024 | 632439 | 18681 | 11137 | 97 | 4715 | 851 | 25 | 33.85 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 197 | The Witcher 3: Wild Hunt | 1 | 2024 | 631209 | 53266 | 4816 | 146 | 6348 | 849 | 71 | 11.85 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 198 | Fallout 4 | 1 | 2024 | 620086 | 65813 | 7649 | 164 | 9732 | 834 | 88 | 9.42 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |
| 199 | Alan Wake II | 1 | 2024 | 616257 | 54513 | 7253 | 190 | 8222 | 829 | 73 | 11.3 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |

### Consulta de celda SQL 8
_Filas exportadas: 105; m?ximo aplicado: 200._

| Year | Month | rows_in_month | distinct_games | best_rank | worst_rank |
| --- | --- | --- | --- | --- | --- |
| 2016 | 1 | 200 | 200 | 1 | 200 |
| 2016 | 2 | 200 | 200 | 1 | 200 |
| 2016 | 3 | 200 | 200 | 1 | 200 |
| 2016 | 4 | 200 | 200 | 1 | 200 |
| 2016 | 5 | 200 | 200 | 1 | 200 |
| 2016 | 6 | 200 | 200 | 1 | 200 |
| 2016 | 7 | 200 | 200 | 1 | 200 |
| 2016 | 8 | 200 | 200 | 1 | 200 |
| 2016 | 9 | 200 | 200 | 1 | 200 |
| 2016 | 10 | 200 | 199 | 1 | 200 |
| 2016 | 11 | 200 | 200 | 1 | 200 |
| 2016 | 12 | 200 | 200 | 1 | 200 |
| 2017 | 1 | 200 | 200 | 1 | 200 |
| 2017 | 2 | 200 | 200 | 1 | 200 |
| 2017 | 3 | 200 | 200 | 1 | 200 |
| 2017 | 4 | 200 | 200 | 1 | 200 |
| 2017 | 5 | 200 | 200 | 1 | 200 |
| 2017 | 6 | 200 | 200 | 1 | 200 |
| 2017 | 7 | 200 | 200 | 1 | 200 |
| 2017 | 8 | 200 | 200 | 1 | 200 |
| 2017 | 9 | 200 | 200 | 1 | 200 |
| 2017 | 10 | 200 | 200 | 1 | 200 |
| 2017 | 11 | 200 | 200 | 1 | 200 |
| 2017 | 12 | 200 | 200 | 1 | 200 |
| 2018 | 1 | 200 | 200 | 1 | 200 |
| 2018 | 2 | 200 | 200 | 1 | 200 |
| 2018 | 3 | 200 | 200 | 1 | 200 |
| 2018 | 4 | 200 | 200 | 1 | 200 |
| 2018 | 5 | 200 | 200 | 1 | 200 |
| 2018 | 6 | 200 | 200 | 1 | 200 |
| 2018 | 7 | 200 | 200 | 1 | 200 |
| 2018 | 8 | 200 | 200 | 1 | 200 |
| 2018 | 9 | 200 | 199 | 1 | 200 |
| 2018 | 10 | 200 | 200 | 1 | 200 |
| 2018 | 11 | 200 | 200 | 1 | 200 |
| 2018 | 12 | 200 | 200 | 1 | 200 |
| 2019 | 1 | 200 | 198 | 1 | 200 |
| 2019 | 2 | 200 | 199 | 1 | 200 |
| 2019 | 3 | 200 | 200 | 1 | 200 |
| 2019 | 4 | 200 | 200 | 1 | 200 |
| 2019 | 5 | 200 | 200 | 1 | 200 |
| 2019 | 6 | 200 | 200 | 1 | 200 |
| 2019 | 7 | 200 | 200 | 1 | 200 |
| 2019 | 8 | 200 | 200 | 1 | 200 |
| 2019 | 9 | 200 | 200 | 1 | 200 |
| 2019 | 10 | 200 | 200 | 1 | 200 |
| 2019 | 11 | 200 | 200 | 1 | 200 |
| 2019 | 12 | 200 | 200 | 1 | 200 |
| 2020 | 1 | 200 | 200 | 1 | 200 |
| 2020 | 2 | 200 | 200 | 1 | 200 |
| 2020 | 3 | 200 | 200 | 1 | 200 |
| 2020 | 4 | 200 | 200 | 1 | 200 |
| 2020 | 5 | 200 | 200 | 1 | 200 |
| 2020 | 6 | 200 | 200 | 1 | 200 |
| 2020 | 7 | 200 | 200 | 1 | 200 |
| 2020 | 8 | 200 | 200 | 1 | 200 |
| 2020 | 9 | 200 | 200 | 1 | 200 |
| 2020 | 10 | 200 | 200 | 1 | 200 |
| 2020 | 11 | 200 | 200 | 1 | 200 |
| 2020 | 12 | 200 | 200 | 1 | 200 |
| 2021 | 1 | 200 | 200 | 1 | 200 |
| 2021 | 2 | 200 | 200 | 1 | 200 |
| 2021 | 3 | 200 | 200 | 1 | 200 |
| 2021 | 4 | 200 | 200 | 1 | 200 |
| 2021 | 5 | 200 | 200 | 1 | 200 |
| 2021 | 6 | 200 | 200 | 1 | 200 |
| 2021 | 7 | 200 | 200 | 1 | 200 |
| 2021 | 8 | 200 | 200 | 1 | 200 |
| 2021 | 9 | 200 | 199 | 1 | 200 |
| 2021 | 10 | 200 | 199 | 1 | 200 |
| 2021 | 11 | 200 | 200 | 1 | 200 |
| 2021 | 12 | 200 | 200 | 1 | 200 |
| 2022 | 1 | 200 | 200 | 1 | 200 |
| 2022 | 2 | 200 | 200 | 1 | 200 |
| 2022 | 3 | 200 | 200 | 1 | 200 |
| 2022 | 4 | 200 | 200 | 1 | 200 |
| 2022 | 5 | 200 | 200 | 1 | 200 |
| 2022 | 6 | 200 | 200 | 1 | 200 |
| 2022 | 7 | 200 | 199 | 1 | 200 |
| 2022 | 8 | 200 | 200 | 1 | 200 |
| 2022 | 9 | 200 | 200 | 1 | 200 |
| 2022 | 10 | 200 | 200 | 1 | 200 |
| 2022 | 11 | 200 | 200 | 1 | 200 |
| 2022 | 12 | 200 | 200 | 1 | 200 |
| 2023 | 1 | 200 | 199 | 1 | 200 |
| 2023 | 2 | 200 | 200 | 1 | 200 |
| 2023 | 3 | 200 | 199 | 1 | 200 |
| 2023 | 4 | 200 | 200 | 1 | 200 |
| 2023 | 5 | 200 | 200 | 1 | 200 |
| 2023 | 6 | 200 | 200 | 1 | 200 |
| 2023 | 7 | 200 | 200 | 1 | 200 |
| 2023 | 8 | 200 | 200 | 1 | 200 |
| 2023 | 9 | 200 | 200 | 1 | 200 |
| 2023 | 10 | 200 | 200 | 1 | 200 |
| 2023 | 11 | 200 | 200 | 1 | 200 |
| 2023 | 12 | 200 | 200 | 1 | 200 |
| 2024 | 1 | 200 | 200 | 1 | 200 |
| 2024 | 2 | 200 | 200 | 1 | 200 |
| 2024 | 3 | 200 | 200 | 1 | 200 |
| 2024 | 4 | 200 | 200 | 1 | 200 |
| 2024 | 5 | 200 | 199 | 1 | 200 |
| 2024 | 6 | 200 | 200 | 1 | 200 |
| 2024 | 7 | 200 | 200 | 1 | 200 |
| 2024 | 8 | 200 | 200 | 1 | 200 |
| 2024 | 9 | 200 | 200 | 1 | 200 |

### Muestra de estructura (una fila)
_Filas exportadas: 1; m?ximo aplicado: 200._

| Rank | Game | Month | Year | Hours_watched | Hours_streamed | Peak_viewers | Peak_channels | Streamers | Avg_viewers | Avg_channels | Avg_viewer_ratio | _ingested_at | _source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | League of Legends | 1 | 2016 | 94377226 | 1362044 | 530270 | 2903 | 129172 | 127021 | 1833 | 69.29 | 2026-09-16 18:47:15.962265 | https://www.kaggle.com/datasets/rankirsh/evolution-of-top-games-on-twitch |

## Hallazgos y conclusiones
Los hallazgos deben interpretarse a partir de los conteos y muestras exportados; esta celda no inventa conclusiones ni marca como aprobada una validaci?n no ejecutada.
