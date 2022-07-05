from decimal import *
from model.customer import Customer
from model.account import Account
from dao.account_dao import AccountDao
from service.customer_service import CustomerService
from exception.exceptions import *


class AccountService:
    def __init__(self):
        self.__account_types = ("savings", "checking", "money market", "certificate of deposit")
        self.account_dao = AccountDao()
        self.customer_service = CustomerService()

    def add_account(self, customer_id, data):
        self.customer_service.get_customer_by_id(customer_id)
        try:
            balance = float(data["balance"])
            if balance < 0:
                raise InvalidParameterError("balance cannot be less than zero")
            elif balance >= 100000000:
                raise InvalidParameterError("balance cannot greater than or equal too 100000000 (that's 8 zeros)")

            account_type = data["account_type"].lower()
            if account_type not in self.__account_types:
                raise InvalidParameterError("account_type must be one of the following " + str(self.__account_types))

            account_added = self.account_dao.add_account(customer_id, data)
            return Account(account_added[0], account_added[1], account_added[2], account_added[3])

        except KeyError as e:
            raise InvalidParameterError(f"parameter {e} was not found")
        except ValueError:
            raise InvalidParameterError(f"'{data['balance']}' is not a valid value for balance")

    def delete_account_by_id(self, customer_id, account_id):
        self.get_account_by_id(customer_id, account_id)
        self.account_dao.delete_account_by_id(customer_id, account_id)

    def get_customer_accounts(self, customer_id):
        self.customer_service.get_customer_by_id(customer_id)
        customer_accounts = self.account_dao.get_customer_accounts(customer_id)
        return customer_accounts

    def get_account_by_id(self, customer_id, account_id):
        self.customer_service.get_customer_by_id(customer_id)
        customer_account = self.account_dao.get_account_by_id(customer_id, account_id)
        if not customer_account:
            raise AccountNotFoundError(f"Customer with id {customer_id} does not have account with id {account_id}")
        return Account(customer_account[0], customer_account[1], customer_account[2], customer_account[3])

    def update_account_by_id(self, customer_id, account_id, data):
        account = self.get_account_by_id(customer_id, account_id)
        try:
            balance = float(data["balance"])
            if balance < 0:
                raise InvalidParameterError("balance cannot be less than zero")
            elif balance >= 100000000:
                raise InvalidParameterError("balance cannot greater than or equal too 100000000 (that's 8 zeros)")
            account.balance = balance
        except KeyError:
            pass
        try:
            account_type = data["account_type"].lower()
            if account_type not in self.__account_types:
                raise InvalidParameterError("account_type must be one of the following " + str(self.__account_types))
            account.account_type = account_type
        except KeyError:
            pass

        updated_account = self.account_dao.update_account(account)
        return Account(updated_account[0], updated_account[1], updated_account[2], updated_account[3])



