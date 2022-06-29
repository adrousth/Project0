class Account:
    def __init__(self, account_id, customer_id, account_type, balance):
        self.account_id = account_id
        self.customer_id = customer_id
        self.account_type = account_type
        self.balance = balance

    def to_dict(self):
        return {
            "account_id": self.account_id,
            "customer_id": self.customer_id,
            "account_type": self.account_type,
            "balance": self.balance
        }

