import psycopg

with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres", password="ButtNugget0104!") as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM customers")
        print(cur.fetchall())

