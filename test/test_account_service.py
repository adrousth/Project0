import pytest
from model.account import Account
from service.account_service import AccountService
from exception.exceptions import *

account_service = AccountService()


# TODO negative tests
def test_get_account_by_id_positive(mocker):
    def mock_get_account_by_id(self, customer_id, account_id):
        if customer_id == 1 and account_id == 20:
            return account_id, 100.00, "checking", customer_id
        else:
            return None

    def mock_get_customer_by_id(self, customer_id):
        if customer_id != 1:
            raise CustomerNotFoundError("Customer not found")

    mocker.patch('service.customer_service.CustomerService.get_customer_by_id', mock_get_customer_by_id)
    mocker.patch('dao.account_dao.AccountDao.get_account_by_id', mock_get_account_by_id)

    actual = account_service.get_account_by_id(1, 20)
    assert Account(20, 100.00, "checking", 1).to_dict() == actual.to_dict()


def test_get_customer_accounts_positive(mocker):
    def mock_get_customer_by_id(self, customer_id):
        if customer_id != 1:
            raise CustomerNotFoundError("Customer not found")

    mocker.patch('service.customer_service.CustomerService.get_customer_by_id', mock_get_customer_by_id)

    def mock_get_customer_accounts(self, customer_id, amount_greater_than, amount_less_than):
        if customer_id == 1:
            return [Account(20, 100.00, "checking", 1).to_dict(), Account(21, 200.00, "savings", 1).to_dict()]

    mocker.patch('dao.account_dao.AccountDao.get_customer_accounts', mock_get_customer_accounts)
    actual = account_service.get_customer_accounts(1, None, None)
    assert [Account(20, 100.00, "checking", 1).to_dict(), Account(21, 200.00, "savings", 1).to_dict()] == actual


def test_get_customer_accounts_positive_range(mocker):
    def mock_get_customer_by_id(self, customer_id):
        if customer_id != 1:
            raise CustomerNotFoundError("Customer not found")

    mocker.patch('service.customer_service.CustomerService.get_customer_by_id', mock_get_customer_by_id)

    def mock_get_customer_accounts(self, customer_id, amount_greater_than, amount_less_than):
        return [Account(20, 100.00, "checking", 1).to_dict(), Account(21, 200.00, "savings", 1).to_dict()]

    mocker.patch('dao.account_dao.AccountDao.get_customer_accounts', mock_get_customer_accounts)
    actual = account_service.get_customer_accounts(1, 50, 300)
    assert [Account(20, 100.00, "checking", 1).to_dict(), Account(21, 200.00, "savings", 1).to_dict()] == actual


def test_get_customer_accounts_negative_range(mocker):
    def mock_get_customer_by_id(self, customer_id):
        if customer_id != 1:
            raise CustomerNotFoundError("Customer not found")

    mocker.patch('service.customer_service.CustomerService.get_customer_by_id', mock_get_customer_by_id)

    def mock_get_customer_accounts(self, customer_id, amount_greater_than, amount_less_than):
        return [Account(20, 100.00, "checking", 1).to_dict(), Account(21, 200.00, "savings", 1).to_dict()]

    mocker.patch('dao.account_dao.AccountDao.get_customer_accounts', mock_get_customer_accounts)
    actual = account_service.get_customer_accounts(1, 'a', 'w')
    assert [Account(20, 100.00, "checking", 1).to_dict(), Account(21, 200.00, "savings", 1).to_dict()] == actual


def test_add_account_positive(mocker):
    def mock_get_customer_by_id(self, customer_id):
        if customer_id != 3:
            raise CustomerNotFoundError("Customer not found")
    mocker.patch('service.customer_service.CustomerService.get_customer_by_id', mock_get_customer_by_id)

    def mock_add_account(self, customer_id, data):
        return 22, data["balance"], data["account_type"], customer_id
    mocker.patch('dao.account_dao.AccountDao.add_account', mock_add_account)

    input_data = {
        "balance": 300,
        "account_type": "checking"
    }

    actual = account_service.add_account(3, input_data)

    assert actual.to_dict() == Account(22, 300, "checking", 3).to_dict()


def test_update_account_by_id(mocker):
    def mock_get_customer_by_id(self, customer_id):
        if customer_id != 1:
            raise CustomerNotFoundError("Customer not found")

    mocker.patch('service.customer_service.CustomerService.get_customer_by_id', mock_get_customer_by_id)


def test_delete_account_by_id(mocker):
    def mock_get_customer_by_id(self, customer_id):
        if customer_id != 1:
            raise CustomerNotFoundError("Customer not found")

    mocker.patch('service.customer_service.CustomerService.get_customer_by_id', mock_get_customer_by_id)






