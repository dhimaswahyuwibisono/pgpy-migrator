import os

def database(SOURCE_DB_PATH, DUMPFILE):
    print("Running pg_dump... This process may take a while, consider running on the compute engine")
    os.system("pg_dump --dbname="+SOURCE_DB_PATH+" --format=plain --no-owner --no-acl | sed -E 's/^(DROP|CREATE|COMMENT ON) EXTENSION/-- \1 EXTENSION/g' > "+DUMPFILE+"")
    return "POSTGRES HAS BEEN DUMPED TO LOCAL"

