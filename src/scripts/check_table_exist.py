
"""Check whether a Unity Catalog table exists.

Expected Databricks Python task parameters:
    --catalog <catalog> --schema <schema> --table <table>
"""

import argparse
import shlex
import sys


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Comprueba si existe una tabla de Unity Catalog."
    )
    parser.add_argument("--catalog", required=True, help="Nombre del catálogo.")
    parser.add_argument("--schema", required=True, help="Nombre del esquema.")
    parser.add_argument("--table", required=True, help="Nombre de la tabla.")
    raw_args = sys.argv[1:] if argv is None else argv
    normalized_args = []
    for argument in raw_args:
        normalized_args.extend(shlex.split(argument))
    return parser.parse_args(normalized_args)


args = parse_args()
catalog = args.catalog.strip()
schema = args.schema.strip()
table = args.table.strip()

if not catalog or not schema or not table:
    raise ValueError("catalog, schema y table no pueden estar vacíos.")

qualified_table = f"`{catalog}`.`{schema}`.`{table}`"

# Verificar si la tabla existe en el catálogo
table_exists = spark.catalog.tableExists(qualified_table)

# Enviar el resultado como un valor del Job
dbutils.jobs.taskValues.set(key="exists", value=str(table_exists).lower())
print(f"{qualified_table}: exists={str(table_exists).lower()}")