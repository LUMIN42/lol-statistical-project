import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
  "host": "webik.ms.mff.cuni.cz",
  "port": 5432,
  "dbname": "ndbi046",
  "user": "stud_75511435",
  "password": "REDACTED",
}


def get_connection():
  return psycopg2.connect(
    host=DB_CONFIG["host"],
    port=DB_CONFIG["port"],
    dbname=DB_CONFIG["dbname"],
    user=DB_CONFIG["user"],
    password=DB_CONFIG["password"],
  )
