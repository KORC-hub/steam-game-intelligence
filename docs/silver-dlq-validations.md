# Validaciones Silver y DLQ

## Principio

Las validaciones se aplican en línea durante los notebooks de
[`src/transformation/`](../src/transformation/). Una fila que
incumple una regla no entra a Silver y se escribe en DLQ con un motivo
explícito. El perfilado de los notebooks de diagnóstico fue la evidencia para fijar el
contrato.

## Orden de procesamiento

Para cada tabla:

1. leer Bronze hasta el cutoff;
2. estandarizar nombres y tipos con `try_*`;
3. evaluar reglas de clave;
4. separar claves inválidas a DLQ;
5. deduplicar determinísticamente las filas que pasaron las claves;
6. marcar las filas superseded como deduplicadas, no como rechazadas;
7. evaluar reglas de negocio en una sola pasada;
8. escribir Silver y DLQ de forma idempotente;
9. verificar la contabilidad.

El orden entre tablas es `games` -> `player_counts_monthly` ->
`twitch_activity_monthly`. Esto permite que una política futura de huérfanos
dependa del catálogo de juegos sin invertir el flujo.

## Reglas implementadas

### `silver.games`

| Regla | Tipo | Predicado de violación | Motivo |
|---|---|---|---|
| `app_id_invalido` | key | `app_id IS NULL OR app_id <= 0` | no existe una clave de juego utilizable |
| `name_vacio` | rule | `name IS NULL OR trim(name) = ''` | impide identificar y relacionar el juego |
| `price_negativo` | rule | `price < 0` | un precio negativo no representa una métrica válida |
| `conteo_negativo` | rule | `positive < 0 OR negative < 0 OR peak_ccu < 0` | métricas de actividad o reviews negativas son inconsistentes |
| `estimated_owners_invalido` | rule | rango informado sin extremos numéricos | evita publicar un rango de propietarios ilegible |

`release_date` futura no se rechaza. El valor cero de puntuaciones se conserva
como válido.

### `silver.player_counts_monthly`

| Regla | Tipo | Predicado de violación | Motivo |
|---|---|---|---|
| `app_id_invalido` | key | `app_id IS NULL OR app_id <= 0` | no existe una clave de juego utilizable |
| `mes_no_parseable` | key | `month_start IS NULL` | no se puede asignar la medición a un mes |
| `jugadores_negativos` | rule | `avg_players < 0 OR peak_players < 0` | los conteos no pueden ser negativos |
| `avg_mayor_que_peak` | rule | `avg_players > peak_players` | el promedio mensual no puede superar el máximo mensual |

Los huérfanos se conservan con `in_catalog = false`; no son rechazo DLQ.

### `silver.twitch_activity_monthly`

| Regla | Tipo | Predicado de violación | Motivo |
|---|---|---|---|
| `fecha_invalida` | key | `month_start IS NULL` | no se puede ubicar la actividad temporalmente |
| `rank_fuera_de_rango` | rule | `twitch_rank IS NULL OR twitch_rank < 1 OR twitch_rank > 200` | la fuente declara un top 200 |
| `game_vacio` | rule | `game IS NULL OR trim(game) = ''` | no hay nombre para inspección o matching |
| `metrica_negativa` | rule | cualquier métrica de audiencia/emisión `< 0` | las métricas negativas son inconsistentes |

Para duplicados Twitch por `(month_start, twitch_rank)`, se conserva la fila
con mayor `hours_watched`; el desempate es por `game_normalized` y luego
`_ingested_at`. Los duplicados descartados no se escriben actualmente en DLQ.
No se rechaza Twitch únicamente por no hacer match con Steam.

## Deduplificación

La deduplicación ocurre después de las reglas de clave:

```text
PARTITION BY clave_de_negocio
ORDER BY _ingested_at DESC, _row_hash DESC
```

La fila con `rn = 1` es la vigente. Las filas con `rn > 1` son superseded:
no se consideran DLQ porque son snapshots anteriores, no necesariamente datos
inválidos.

## Motivos y estructura DLQ

Si una fila viola varias reglas, se crea un solo registro DLQ:

- `motivo_rechazo`: reglas unidas con `; `;
- `reglas_violadas`: array de nombres de regla;
- `payload`: JSON del staging;
- `_reject_key`: hash determinista de la clave y el payload;
- `_run_id` y `_rejected_at`.

La implementación actual reconstruye la tabla DLQ con `CREATE OR REPLACE TABLE`
para mantenerla alineada con el estado rechazado de la fuente al cutoff actual.

## Contabilidad obligatoria

Por tabla debe cumplirse:

```text
n_in = n_key_rej + n_superseded + n_rule_rej + n_silver
```

Después de escribir:

```text
COUNT(Silver) = n_silver
COUNT(DLQ) + n_exact_dups_collapsed = n_key_rej + n_rule_rej
```

Si la contabilidad no cuadra, el notebook debe fallar explícitamente. No se
debe presentar una ejecución incompleta como exitosa.

## Perfilado relacionado

Los notebooks de diagnóstico existentes ya consultan:

- nulos por columna;
- duplicados por clave y día/mes;
- valores fuera de rango;
- formatos de `month`;
- formatos de `gain`;
- métricas negativas;
- muestras de filas problemáticas;
- variaciones entre snapshots;
- cobertura temporal.

Esos notebooks sirven para explicar por qué cada regla es pertinente, pero no
autorizan por sí solos a fijar umbrales. Una regla con cero violaciones puede
conservarse si es pertinente, demostrando su comportamiento con un registro
controlado en sandbox, tal como exige el plan.
