import csv

from db import get_connection

# normally, I'd also do a group by here, but I want the code to be reproducible without the SQL
with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT win, dragon_kills
            FROM dim_objectives;
            """
        ) # grouped by team in the data by default

        rows = cur.fetchall()
        headers = [desc[0] for desc in cur.description]

with open("dragon_soul_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

