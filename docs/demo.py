import psycopg2

conn = psycopg2.connect("dbname=test user=postgres")
cur = conn.cursor()

query = """
SELECT last_name,
    start_day,
    COUNT(*) AS num_entries
FROM schema.table -- great name!
WHERE start_day >= '2019-01-01'
GROUP BY last_name, start_day
ORDER BY num_entries DESC
LIMIT 10;
"""

cur.execute(query)
first_row = cur.fetchone()
