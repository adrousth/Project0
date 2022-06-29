from model.customer import Customer


class CustomerDao:
    def __init__(self):
        pass

    def get_all_customers(self):
        print("get all customers")
        return {}

    def get_customer_by_id(self, customer_id):
        print("customer id:", customer_id)
        return {}

    def add_customer(self, data):
        print("customer:", data)
        return {}

    def delete_customer(self, customer_id):
        print("delete customer id:", customer_id)
        return {}

    def update_customer(self, customer_id):
        print("updating customer:", customer_id)
        return {}