import csv

from db import get_connection

with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT win,
                (
                    COUNT(*) FILTER (WHERE adaptivetype = 'Physical') >= 4
                    OR
                    COUNT(*) FILTER (WHERE adaptivetype = 'Magical') >= 4
                )
                AS skewed
            FROM fact_participants p
            JOIN dim_champions c
            ON p.champion_name = c.apiname
            GROUP BY team_id, win
            """
        )

        rows = cur.fetchall()
        headers = [desc[0] for desc in cur.description]

with open("ap_ad_split.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)
