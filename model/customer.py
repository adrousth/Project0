class Customer:

    def __init__(self, customer_id, first_name, last_name):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        return {
            "customer id": self.customer_id,
            "first name": self.first_name,
            "last name": self.last_name
        }

