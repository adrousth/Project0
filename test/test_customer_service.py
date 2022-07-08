import pytest
from model.customer import Customer
from service.customer_service import CustomerService
from exception.exceptions import *


customer_service = CustomerService()


def test_get_all_customers(mocker):

    def mock_get_all_customers(self):
        return [Customer(1, 'test123', 'customer123').to_dict(), Customer(2, 'testing123', 'customer456').to_dict()]

    mocker.patch('dao.customer_dao.CustomerDao.get_all_customers', mock_get_all_customers)
    actual = customer_service.get_all_customers()
    assert actual == [
        {
            "customer id": 1,
            "first name": "test123",
            "last name": "customer123",
        },
        {
            "customer id": 2,
            "first name": "testing123",
            "last name": "customer456",
        }
    ]


def test_get_customer_by_id_positive(mocker):
    def mock_get_customer_by_id(self, customer_id):
        if customer_id == 1:
            return 1, 'test123', 'customer123'
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    actual = customer_service.get_customer_by_id(1)

    assert actual.to_dict() == Customer(1, 'test123', 'customer123').to_dict()


def test_get_customer_by_id_negative(mocker):
    def mock_get_customer_by_id(self, customer_id):
        if customer_id == 1:
            return 1, 'test123', 'customer123'
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)

    with pytest.raises(CustomerNotFoundError) as exception_info:
        customer_service.get_customer_by_id(100)
    assert str(exception_info.value) == "Customer with id 100 was not found"


def test_update_customer_positive(mocker):
    def mock_update_customer(self, customer):
        return customer.customer_id, customer.first_name, customer.last_name

    def mock_get_customer_by_id(self, customer_id):
        if customer_id == 11:
            return 11, "John", "West"
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.update_customer', mock_update_customer)
    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)

    data = {
        "first_name": "Jimmy",
        "last_name": "Johnson"
    }
    actual = customer_service.update_customer(11, data)
    assert actual.to_dict() == Customer(11, "Jimmy", "Johnson").to_dict()


def test_update_customer_negative_id(mocker):
    def mock_get_customer_by_id(self, customer_id):
        if customer_id == 11:
            return 11, "John", "West"
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    data = {
        "first_name": "Jimmy",
        "last_name": "Johnson"
    }
    with pytest.raises(CustomerNotFoundError) as exception_info:
        customer_service.update_customer(110, data)
    assert str(exception_info.value) == "Customer with id 110 was not found"


def test_update_customer_negative_first_name(mocker):
    def mock_get_customer_by_id(self, customer_id):
        if customer_id == 11:
            return 11, "John", "West"
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    data = {
        "first_name": "J",
        "last_name": "Johnson"
    }
    with pytest.raises(InvalidParameterError) as exception_info:
        customer_service.update_customer(11, data)
    assert str(exception_info.value) == "first name must be at least 2 characters long"

    data["first_name"] = "hereismyreallyreallylongfirstnamethatisreallywaytoolong"
    with pytest.raises(InvalidParameterError) as exception_info:
        customer_service.update_customer(11, data)
    assert str(exception_info.value) == "first name cannot be more than 50 characters long"


def test_update_customer_negative_last_name(mocker):
    def mock_get_customer_by_id(self, customer_id):
        if customer_id == 11:
            return 11, "John", "West"
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    data = {
        "first_name": "Jimmy",
        "last_name": "J"
    }
    with pytest.raises(InvalidParameterError) as exception_info:
        customer_service.update_customer(11, data)
    assert str(exception_info.value) == "last name must be at least 2 characters long"

    data["last_name"] = "hereismyreallyreallylonglastnamethatisreallywaytoolong"
    with pytest.raises(InvalidParameterError) as exception_info:
        customer_service.update_customer(11, data)
    assert str(exception_info.value) == "last name cannot be more than 50 characters long"






def test_add_customer_positive(mocker):
    def mock_add_customer(self, data):
        return 10, data["first_name"], data["last_name"]

    mocker.patch('dao.customer_dao.CustomerDao.add_customer', mock_add_customer)
    data = {
        "first_name": "Joe",
        "last_name": "Smith"
    }
    actual = customer_service.add_customer(data)
    assert actual.to_dict() == Customer(10, "Joe", "Smith").to_dict()


def test_add_customer_negative_first_name(mocker):
    data = {
        "first_name": "J",
        "last_name": "Smith"
    }

    with pytest.raises(InvalidParameterError) as exception_info:
        customer_service.add_customer(data)
    assert str(exception_info.value) == "first name must be at least 2 characters long"

    data["first_name"] = "hereismyreallyreallylongfirstnamethatisreallywaytoolong"
    with pytest.raises(InvalidParameterError) as exception_info:
        customer_service.add_customer(data)
    assert str(exception_info.value) == "first name cannot be more than 50 characters long"


def test_add_customer_negative_last_name(mocker):
    data = {
        "first_name": "Joe",
        "last_name": "S"
    }

    with pytest.raises(InvalidParameterError) as exception_info:
        customer_service.add_customer(data)
    assert str(exception_info.value) == "last name must be at least 2 characters long"

    data["last_name"] = "hereismyreallyreallylonglastnamethatisreallywaytoolong"
    with pytest.raises(InvalidParameterError) as exception_info:
        customer_service.add_customer(data)
    assert str(exception_info.value) == "last name cannot be more than 50 characters long"


def test_add_customer_negative_lacking_parameter(mocker):
    data = {
        "last_name": "Smith"
    }

    with pytest.raises(InvalidParameterError) as exception_info:
        customer_service.add_customer(data)
    assert str(exception_info.value) == "parameter 'first_name' was not found"

    data = {
        "first_name": "Joe"
    }
    with pytest.raises(InvalidParameterError) as exception_info:
        customer_service.add_customer(data)
    assert str(exception_info.value) == "parameter 'last_name' was not found"






def test_delete_customer_by_id_positive(mocker):
    def mock_delete_customer(self, customer_id):
        if customer_id == 12:
            return True
        else:
            return False

    mocker.patch('dao.customer_dao.CustomerDao.delete_customer', mock_delete_customer)
    assert customer_service.delete_customer_by_id(12)


def test_delete_customer_by_id_negative(mocker):
    def mock_delete_customer(self, customer_id):
        if customer_id == 12:
            return True
        else:
            return False

    mocker.patch('dao.customer_dao.CustomerDao.delete_customer', mock_delete_customer)
    with pytest.raises(CustomerNotFoundError) as exception_info:
        customer_service.delete_customer_by_id(120)
    assert str(exception_info.value) == "Customer with id 120 was not found"


