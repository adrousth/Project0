from model.customer import Customer
import psycopg


class CustomerDao:
    def __init__(self):
        self.__connection_string = "host=localhost port=5432 dbname=postgres user=postgres password=ButtNugget0412!"

    def get_all_customers(self):
        with psycopg.connect(self.__connection_string) as conn:
            with conn.cursor() as cur:
                print(cur)
                cur.execute("SELECT * FROM customers")
                all_customers = cur.fetchall()
        return all_customers

    def get_customer_by_id(self, customer_id):
        print("customer id:", customer_id)
        with psycopg.connect(self.__connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers WHERE id = %s",
                            (customer_id,))
                customer = cur.fetchone()
        return customer

    def add_customer(self, data):
        print("customer:", data)
        with psycopg.connect(self.__connection_string) as conn:
            with conn.cursor() as cur:
                pass
        return {}

    def delete_customer(self, customer_id):
        print("delete customer id:", customer_id)
        with psycopg.connect(self.__connection_string) as conn:
            with conn.cursor() as cur:
                pass
        return {}

    def update_customer(self, customer_id):
        print("updating customer:", customer_id)
        with psycopg.connect(self.__connection_string) as conn:
            with conn.cursor() as cur:
                pass
        return {}
