from exception.exceptions import *

from flask import request, Blueprint
from model.customer import Customer
from service.customer_service import CustomerService

ctrl = Blueprint('controller', __name__)
customer_service = CustomerService()


# POST /customers: Creates a new customer
@ctrl.route("/customers", methods=["POST"])
def add_customer():
    print("add customer")
    data = request.get_json()
    customer_service.add_customer(data)
    return {}


# GET /customers: Gets all customers

@ctrl.route("/customers", methods=["GET"])
def get_all_customers():
    print("get all customers")
    return {}


# GET /customer/{customer_id}: Get customer with an id of X (if the customer exists)
@ctrl.route("/customer/<customer_id>", methods=["GET"])
def get_customer_by_id(customer_id):
    print("get customer by id:", customer_id)
    try:
        return customer_service.get_user_by_id(customer_id)  # dictionary
    except CustomerNotFoundError as e:
        return {
                   "message": str(e)
               }, 404


# PUT /customer/{customer_id}: Update customer with an id of X (if the customer exists)
@ctrl.route("/customer/<customer_id>", methods=["PUT"])
def update_customer_by_id(customer_id):
    print("update customer by id:", customer_id)

    try:
        data = request.get_json()
        print(data)
        return customer_service.update_user_by_id(Customer(customer_id, data['first_name'], data['last_name']))
    except CustomerNotFoundError as e:
        return {
                   "message": str(e)
               }, 404

# DELETE /customer/{customer_id}: Delete customer with an id of X (if the customer exists)
@ctrl.route("/customer/<customer_id>", methods=["DELETE"])
def delete_customer_by_id(customer_id):
    print("delete customer by id:", customer_id)
    return {}


# POST /customer/{customer_id}/accounts: Create a new account for a customer with id of X (if customer exists)
@ctrl.route("/customer/<customer_id>/accounts", methods=["POST"])
def create_account(customer_id):
    print("create account for id:", customer_id)
    data = request.get_json()
    print(data)
    return {}


# check for query parameters using ctx.queryParam("amountLessThan") / ctx.queryParam("amountGreaterThan)
# GET /customer/{customer_id}/accounts: Get all accounts for customer with id of X (if customer exists)
# GET /customer/{customer_id}/accounts?amountLessThan=1000&amountGreaterThan=300:
# Get all accounts for customer id of X with balances between Y and Z (if customer exists)
@ctrl.route("/customer/<customer_id>/accounts", methods=["GET"])
def get_customer_accounts(customer_id):
    amount_greater_than = request.args.get("amountGreaterThan")
    amount_less_than = request.args.get("amountLessThan")
    print("get customer accounts:", customer_id)
    print("account balance greater than:", amount_greater_than)
    print("account balance less than:", amount_less_than)
    return {}


# GET /customer/{customer_id}/account/{account_id}: Get account with id of Y belonging to customer with id of X
# (if customer and account exist AND if account belongs to customer)
@ctrl.route("/customer/<customer_id>/account/<account_id>", methods=["GET"])
def get_account_by_id(customer_id, account_id):
    customer = get_customer_by_id(customer_id)
    print("get account by id:", account_id)
    return {}


# PUT /customer/{customer_id}/account/{account_id}: Update account with id of Y belonging to customer with id of X
# (if customer and account exist AND if account belongs to customer)
@ctrl.route("/customer/<customer_id>/account/<account_id>", methods=["PUT"])
def update_account_by_id(customer_id, account_id):
    customer = get_customer_by_id(customer_id)
    print("update account by id:", account_id)
    data = request.get_json()
    print(data)
    return {}


# DELETE /customer/{customer_id}/account/{account_id}: Delete account with id of Y belonging to customer with id of X
# (if customer and account exist AND if account belongs to customer)
@ctrl.route("/customer/<customer_id>/account/<account_id>", methods=["DELETE"])
def delete_account_by_id(customer_id, account_id):
    customer = get_customer_by_id(customer_id)
    print("delete account by id:", account_id)
    return {}

