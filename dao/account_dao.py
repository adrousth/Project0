from model.account import Account
import psycopg


class AccountDao:

    def __init__(self):
        self.__connection_string = "host=localhost port=5432 dbname=postgres user=postgres password=ButtNugget0412!"

    def add_account(self, customer_id, data):
        with psycopg.connect(self.__connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO accounts (balance, account_type, customer_id) VALUES (%s, %s, %s) RETURNING *",
                            (data["balance"], data["account_type"], customer_id))
                account_added = cur.fetchone()
                conn.commit()
        return account_added

    def get_customer_accounts(self, customer_id):
        with psycopg.connect(self.__connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts WHERE customer_id = %s",
                            (customer_id,))
                customer_accounts = cur.fetchall()
        return customer_accounts

    def get_account_by_id(self, customer_id, account_id):
        with psycopg.connect(self.__connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts WHERE id = %s AND customer_id = %s",
                            (account_id, customer_id,))
                account = cur.fetchone()
        return account

    def update_account(self, account):
        with psycopg.connect(self.__connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE accounts SET balance = %s, account_type = %s WHERE id = %s RETURNING *",
                            (account.balance, account.account_type, account.account_id))
                updated_account = cur.fetchone()
                conn.commit()
        return updated_account

    def delete_account_by_id(self, customer_id, account_id):
        with psycopg.connect(self.__connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM accounts WHERE id = %s AND customer_id = %s", (account_id, customer_id))
                if cur.rowcount != 1:
                    return False
                else:
                    conn.commit()
                    return True

