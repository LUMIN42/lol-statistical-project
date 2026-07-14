import csv

from db import get_connection

FRIEND_ID = "DSL0IvMCAEknDhsABcx7E2jRxITU02X9wN1ynAvFG2cbZI9uD7YqPAOJEYlWgkRYsI7AOar6tGrB9w"
MY_ID = "Dr7nrVxfayEjaHQPCaRQ4dIRS7UDvCmbMdb-Ign20i3aozQ1lZ6O9EXJcE9DP3_L7t_HI4MlfWnLaw"

with get_connection() as conn:
  with conn.cursor() as cur:
    cur.execute(
      """
      SELECT win, BOOL_OR(user_id = %s) AS with_friend
      FROM fact_participants
      GROUP BY team_id, win
      HAVING BOOL_OR(user_id = %s)
      """,
      (FRIEND_ID, MY_ID)
    )

    rows = cur.fetchall()
    headers = [desc[0] for desc in cur.description]

with open("friend_data.csv", "w", newline="", encoding="utf-8") as f:
  writer = csv.writer(f)
  writer.writerow(headers)
  writer.writerows(rows)
