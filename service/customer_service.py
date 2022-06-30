from dao.customer_dao import CustomerDao
from model.customer import Customer
from dao.account_dao import AccountDao
from exception.exceptions import *


class CustomerService:
    def __init__(self):
        self.customer_dao = CustomerDao()

    def get_all_customers(self):
        list_of_customers = self.customer_dao.get_all_customers()
        return list(map(lambda x: x.to_dict(), list_of_customers))

    def add_customer(self, customer):
        self.customer_dao.add_customer(customer)

    def update_customer(self, customer):
        self.customer_dao.update_customer(customer)

    def get_customer_by_id(self, customer_id):
        customer = self.customer_dao.get_customer_by_id(customer_id)
        if not customer:
            raise CustomerNotFoundError(f"User with id {customer_id} was not found")
        return customer.to_dict()

    def delete_customer_by_id(self, customer_id):
        self.customer_dao.delete_customer(customer_id)
