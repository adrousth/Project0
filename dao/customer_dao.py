from model.customer import Customer
import psycopg


class CustomerDao:
    def __init__(self):
        self.__connection_string = "host=localhost port=5432 dbname=postgres user=postgres password=ButtNugget0412!"

    def get_all_customers(self):
        with psycopg.connect(self.__connection_string) as conn:
            with conn.cursor() as cur:
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
                cur.execute("INSERT INTO customers (first_name, last_name) VALUES (%s, %s) RETURNING *",
                            (data["first_name"], data["last_name"]))
                customer_added = cur.fetchone()
                conn.commit()
        return customer_added

    # TODO delete customer's accounts
    def delete_customer(self, customer_id):
        print("delete customer id:", customer_id)
        with psycopg.connect(self.__connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM accounts WHERE customer_id = %s", (customer_id,))
                cur.execute("DELETE FROM customers WHERE id = %s", (customer_id,))
                if cur.rowcount != 1:
                    return False
                else:
                    conn.commit()
                    return True

    def update_customer(self, customer):
        print("updating customer:", customer.customer_id)
        with psycopg.connect(self.__connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE customers SET first_name = %s, last_name = %s WHERE id = %s RETURNING *",
                            (customer.first_name, customer.last_name, customer.customer_id))
                updated_customer = cur.fetchone()
                conn.commit()
        return updated_customer

