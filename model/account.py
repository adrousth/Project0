class Account:
    def __init__(self, account_id, balance, account_type, customer_id):
        self.account_id = account_id
        self.balance = balance
        self.account_type = account_type
        self.customer_id = customer_id

    def to_dict(self):
        return {
            "account_id": self.account_id,
            "balance": self.balance,
            "account_type": self.account_type,
            "customer_id": self.customer_id,
        }

