import psycopg


class User:
    def __init__(self, data):
        self.user_id = data[0]
        self.first_name = data[1]
        self.last_name = data[2]

    def __str__(self):
        return f"user id: {self.user_id}, first name: {self.first_name}, last name: {self.last_name}"


with psycopg.connect("host=localhost port=5432 dbname=postgres user=postgres password=ButtNugget0412!") as conn:

    print(conn)

    with conn.cursor() as cur:
        cur.execute("insert into users (first_name, last_name) values (%s, %s) returning *", ('testing', 'name'))
        user = User(cur.fetchone())

    print(user)




