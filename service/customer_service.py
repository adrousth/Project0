from dao.customer_dao import CustomerDao
from model.customer import Customer
from dao.account_dao import AccountDao
from exception.exceptions import *


class CustomerService:
    def __init__(self):
        self.customer_dao = CustomerDao()

    def get_all_customers(self):
        list_of_customers = self.customer_dao.get_all_customers()
        return list_of_customers

    def add_customer(self, data):
        try:
            if len(data["first_name"]) < 2:
                raise InvalidParameterError("first name must be at least 2 characters long")
            elif len(data["first_name"]) > 50:
                raise InvalidParameterError("first name cannot be more than 50 characters long")

            if len(data["last_name"]) < 2:
                raise InvalidParameterError("last name must be at least 2 characters long")
            elif len(data["last_name"]) > 50:
                raise InvalidParameterError("first name cannot be more than 50 characters long")

            customer_added = self.customer_dao.add_customer(data)
            return Customer(customer_added[0], customer_added[1], customer_added[2])

        except KeyError as e:
            raise InvalidParameterError(f"parameter {e} was not found")

    def update_customer(self, customer_id, data):
        customer = self.get_customer_by_id(customer_id)
        try:
            if len(data["first_name"]) < 2:
                raise InvalidParameterError("first name must be at least 2 characters long")
            elif len(data["first_name"]) > 50:
                raise InvalidParameterError("first name cannot be more than 50 characters long")
            customer.first_name = data["first_name"]
        except KeyError:
            pass
        try:
            if len(data["last_name"]) < 2:
                raise InvalidParameterError("last name must be at least 2 characters long")
            elif len(data["last_name"]) > 50:
                raise InvalidParameterError("first name cannot be more than 50 characters long")
            customer.last_name = data["last_name"]
        except KeyError:
            pass

        updated_customer = self.customer_dao.update_customer(customer)
        return Customer(updated_customer[0], updated_customer[1], updated_customer[2])

    def get_customer_by_id(self, customer_id):
        customer = self.customer_dao.get_customer_by_id(customer_id)
        if not customer:
            raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")
        return Customer(customer[0], customer[1], customer[2])

    def delete_customer_by_id(self, customer_id):
        if not self.customer_dao.delete_customer(customer_id):
            raise CustomerNotFoundError(f"User with id {customer_id} was not found")


