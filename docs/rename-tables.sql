-- Renombrado de objetos existentes en Unity Catalog.
-- Ejecutar una sola vez, después de verificar las tablas actuales.
-- Este bloque asume que las tablas Bronze todavía conservan sus nombres
-- originales de ingesta.
-- No crea tablas ni elimina datos.

USE CATALOG steam_game_intelligence;

-- Bronze: sistema fuente + entidad + modalidad de carga.
ALTER TABLE bronze.steam_games
RENAME TO bronze.steam_games_batch;

ALTER TABLE bronze.steam_games_review
RENAME TO bronze.steam_game_reviews_batch;

ALTER TABLE bronze.steamcharts_2025_history_data
RENAME TO bronze.steamcharts_player_counts_monthly;

ALTER TABLE bronze.twitch_top_200_games_data
RENAME TO bronze.twitch_top_games_monthly;

-- Silver: entidad normalizada y grano de negocio.
ALTER TABLE silver.games
RENAME TO silver.steam_games;

ALTER TABLE silver.player_counts_monthly
RENAME TO silver.steam_player_counts_monthly;

ALTER TABLE silver.twitch_activity_monthly
RENAME TO silver.twitch_game_activity_monthly;

-- DLQ: nombre lógico de Silver más el sufijo de rechazo.
ALTER TABLE dlq.games_rejected
RENAME TO dlq.steam_games_rejected;

ALTER TABLE dlq.player_counts_monthly_rejected
RENAME TO dlq.steam_player_counts_monthly_rejected;

ALTER TABLE dlq.twitch_activity_monthly_rejected
RENAME TO dlq.twitch_game_activity_monthly_rejected;

-- Verificación posterior.
SHOW TABLES IN bronze;
SHOW TABLES IN silver;
SHOW TABLES IN dlq;

-- Si ya ejecutaste la versión anterior de este archivo y Bronze tiene
-- nombres terminados en _snapshot, ejecuta solamente estas dos sentencias
-- alternativas en lugar de las dos primeras sentencias Bronze anteriores:
--
-- ALTER TABLE bronze.steam_games_snapshot
-- RENAME TO bronze.steam_games_batch;
--
-- ALTER TABLE bronze.steam_game_reviews_snapshot
-- RENAME TO bronze.steam_game_reviews_batch;
