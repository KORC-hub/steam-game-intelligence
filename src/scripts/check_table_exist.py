

catalog = "stea"
schema = "mi_esquema"
table = "mi_tabla"

# Verificar si la tabla existe en el catálogo
table_exists = spark.catalog.tableExists(f"{catalog}.{schema}.{table}")

# Enviar el resultado como un valor del Job
dbutils.jobs.taskValues.set(key="exists", value=str(table_exists).lower())