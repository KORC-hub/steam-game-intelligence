# Pruebas de idempotencia

## Objetivo

La prueba verifica que ejecutar dos veces el flujo completo con los mismos
datos de entrada y el mismo corte de Bronze produzca el mismo estado lógico en
Silver, DLQ y Gold. La prueba no busca demostrar que el pipeline sea
inmutable: las tablas Delta pueden registrar una nueva versión, pero el
contenido visible debe mantenerse consistente y no debe acumular duplicados.

El procedimiento está implementado en
[`notebooks/idempotency_tests.ipynb`](../notebooks/idempotency_tests.ipynb).

## Aislamiento mediante sandbox

La prueba lee Bronze desde el catálogo fuente, pero escribe en un catálogo
sandbox independiente. Por defecto utiliza:

```text
source_catalog  = steam_game_intelligence
sandbox_catalog = steam_game_intelligence_sbx
```

Dentro del catálogo sandbox se crean:

```text
steam_game_intelligence_sbx.bronze_sbx
steam_game_intelligence_sbx.silver_sbx
steam_game_intelligence_sbx.dlq_sbx
steam_game_intelligence_sbx.gold_sbx
steam_game_intelligence_sbx.audit_sbx
```

El notebook copia a `bronze_sbx` las fuentes necesarias:

- `steam_games_batch`, filtrada de forma determinista con `app_id % 20 = 0`;
- `steamcharts_player_counts_monthly`, filtrada con
  `steam_appid % 20 = 0`;
- `twitch_top_games_monthly`, sin aplicar ese filtro.

La tabla `steam_game_reviews_batch` se copia completa y participa en la prueba Silver/DLQ. La ingesta Bronze permanece desactivada:
`run_ingestion=false`.

## Parámetros de ejecución

Los widgets del notebook permiten configurar:

| Widget | Valor por defecto | Uso |
|---|---:|---|
| `source_catalog` | `steam_game_intelligence` | Catálogo principal desde el que se lee Bronze |
| `sandbox_catalog` | `steam_game_intelligence_sbx` | Catálogo aislado donde se crean y escriben las tablas |
| `orchestrator_path` | `./silver_orquestator` | Ruta del orquestador en el Git Folder |
| `sandbox_suffix` | `_sbx` | Sufijo de aislamiento |
| `timeout_seconds` | `3600` | Tiempo máximo para cada ejecución |
| `run_mutation_tests` | `false` | Mantiene desactivada la mutación opcional |
| `cleanup_sandbox` | `false` | Conserva los esquemas para inspección posterior |
| `reset_sandbox_catalog` | `false` | Elimina y recrea el catálogo sandbox antes de copiar Bronze |

El notebook calcula una sola vez `cutoff_us` y lo pasa a las dos ejecuciones.
Cada ejecución recibe un `run_id` distinto para distinguirlas en los metadatos,
pero esto no debe cambiar el contenido lógico de las tablas.

## Secuencia de la prueba

### 1. Preparar los esquemas

Se ejecuta `CREATE SCHEMA IF NOT EXISTS` para cada esquema sandbox. Después se
reconstruyen las cuatro tablas Bronze sandbox a partir de las tablas Bronze
existentes.

La copia es deliberadamente determinista. Si se necesita repetir la prueba
desde cero, se debe activar `reset_sandbox_catalog=true`. El notebook ejecuta
`DROP CATALOG <sandbox_catalog> CASCADE`, recrea el catálogo y vuelve a copiar
Bronze. Esta opción solo se acepta para catálogos cuyo nombre termina en
`_sbx` y nunca cuando coincide con `source_catalog`.

### 2. Ejecutar el orquestador por primera vez

El notebook llama a
[`notebooks/silver_orquestator.ipynb`](../notebooks/silver_orquestator.ipynb)
con los esquemas sandbox y el `cutoff_us` común. El orquestador ejecuta
secuencialmente:

```text
crear_schemas
  -> silver.steam_games y DLQ games
  -> silver.steam_player_counts_monthly y DLQ correspondiente
  -> silver.twitch_game_activity_monthly y DLQ correspondiente
  -> Gold (`src/gold_tables`)
```

La primera ejecución sirve como estado de referencia.

### 3. Calcular la referencia

Para cada tabla de Silver, DLQ y Gold se calcula:

- cantidad de filas;
- huella agregada basada en `xxhash64` de cada registro.

La huella excluye los metadatos que cambian entre ejecuciones:

```text
_run_id
_rejected_at
generated_at
```

Por ello, la comparación evalúa el contenido de negocio y no las marcas de
tiempo o identificadores técnicos de la ejecución.

### 4. Ejecutar el orquestador por segunda vez

Se vuelve a ejecutar el mismo orquestador con exactamente el mismo:

- catálogo;
- esquemas sandbox;
- `cutoff_us`;
- contenido Bronze sandbox.

El `run_id` cambia intencionalmente. Después se calculan de nuevo los conteos y
las huellas.

La prueba T1 pasa solamente si el conteo y la huella de cada tabla coinciden
con la referencia.

## Validaciones realizadas

### T1: mismo contenido después de repetir la ejecución

Se comparan conteo y huella para:

```text
silver.steam_games
silver.steam_player_counts_monthly
silver.twitch_game_activity_monthly
dlq.steam_games_rejected
dlq.steam_player_counts_monthly_rejected
dlq.twitch_game_activity_monthly_rejected
gold.game_growth
gold.twitch_steam_relationship
gold.dim_game
```

Esta validación comprueba que una segunda ejecución no agregue filas ni altere
el resultado lógico cuando la fuente y el corte son iguales.

### T2: unicidad de claves en Silver y Gold

Se cuentan grupos con más de una fila para las claves de negocio documentadas:

| Tabla | Clave comprobada |
|---|---|
| `silver.steam_games` | `app_id` |
| `silver.steam_player_counts_monthly` | `(app_id, month_start)` |
| `silver.twitch_game_activity_monthly` | `(month_start, twitch_rank)` |
| `gold.game_growth` | `(app_id, month_start)` |
| `gold.twitch_steam_relationship` | `(app_id, month_start)` |
| `gold.dim_game` | `app_id` |

La prueba pasa cuando no existen grupos duplicados.

### T3: unicidad de rechazados en DLQ

Para cada tabla DLQ se agrupa por `_reject_key` y se buscan grupos con más de
una fila:

```text
dlq.steam_games_rejected
dlq.steam_player_counts_monthly_rejected
dlq.twitch_game_activity_monthly_rejected
```

La prueba pasa cuando cada `_reject_key` aparece como máximo una vez. Esto
comprueba que las filas rechazadas no se dupliquen al repetir el procesamiento.

### T4: historial de Delta

Para cada tabla objetivo se consulta `DESCRIBE HISTORY` y se imprimen las tres
versiones más recientes junto con el mapa real de `operationMetrics`.

El notebook no asume nombres concretos para las métricas porque pueden variar
entre versiones de Databricks Runtime. Esta salida permite revisar el tipo de
operación y la cantidad de filas afectadas en la ejecución real.

## Resultado esperado

Una ejecución correcta debe mostrar:

```text
PASS T1: ...
PASS T2: ...
PASS T3: ...
PASS T4: historial inspeccionado ...
SKIPPED T5: run_mutation_tests=false ...
```

`PASS` significa que la comprobación programada se cumplió en el workspace.
No se debe declarar la prueba como exitosa únicamente porque el notebook sea
válido localmente; es necesario conservar la salida de la ejecución de
Databricks.

## Alcance actual y limitaciones

- La prueba T1 comprueba repetición con el mismo corte y la misma fuente; no
  comprueba todavía el reemplazo de una fila Bronze por una versión actualizada.
- T5 está desactivada por defecto y actualmente queda como una prueba opcional
  pendiente de implementar de forma controlada. Si se activa en la versión
  actual, el notebook detiene la ejecución con `NotImplementedError` para evitar
  mutaciones no confirmadas.
- El notebook actual no automatiza una conciliación completa de entradas,
  rechazados, deduplicaciones y filas aprobadas. Esa contabilidad debe
  complementarse si se necesita evidencia detallada de cada etapa.
- `cleanup_sandbox=false` permite revisar las tablas y el historial después de
  la prueba. Con `cleanup_sandbox=true` se elimina el catálogo sandbox
  completo mediante `DROP CATALOG ... CASCADE`.
- Los cambios en el historial Delta entre ejecuciones son esperables; la
  condición de idempotencia se evalúa sobre el estado lógico visible, no sobre
  la igualdad de números de versión Delta.

## Ejecución recomendada

1. Abrir `notebooks/idempotency_tests.ipynb` en Databricks.
2. Confirmar que `orchestrator_path` apunta a `./silver_orquestator`.
3. Mantener `run_mutation_tests=false`.
4. Mantener `cleanup_sandbox=false` y `reset_sandbox_catalog=false` durante la
   primera validación.
5. Ejecutar todas las celdas en orden.
6. Guardar la salida con los mensajes T1–T4 y el historial Delta.
7. Revisar las tablas sandbox antes de eliminarlas.
8. Para empezar de cero, ejecutar otra corrida con
   `reset_sandbox_catalog=true`. Para eliminarlo al finalizar, usar
   `cleanup_sandbox=true` solo cuando ya no se necesite inspeccionar el sandbox.
