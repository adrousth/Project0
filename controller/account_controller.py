from exception.exceptions import *
from dao.customer_dao import CustomerDao

from flask import request, Blueprint
from service.customer_service import CustomerService
from service.account_service import AccountService

account_ctrl = Blueprint('account_controller', __name__)
customer_service = CustomerService()
account_service = AccountService()


# POST /customer/{customer_id}/accounts: Create a new account for a customer with id of X (if customer exists)
@account_ctrl.route("/customer/<customer_id>/accounts", methods=["POST"])
def add_account(customer_id):
    data = request.get_json()
    try:
        account = account_service.add_account(customer_id, data)
        return account.to_dict(), 202
    except CustomerNotFoundError as e:
        return {
                   "message": str(e)
               }, 404
    except InvalidParameterError as e:
        return {
            "message": str(e)
        }, 400


# check for query parameters using ctx.queryParam("amountLessThan") / ctx.queryParam("amountGreaterThan)
# GET /customer/{customer_id}/accounts: Get all accounts for customer with id of X (if customer exists)
# GET /customer/{customer_id}/accounts?amountLessThan=1000&amountGreaterThan=300:
# Get all accounts for customer id of X with balances between Y and Z (if customer exists)
# TODO add range functionality
@account_ctrl.route("/customer/<customer_id>/accounts", methods=["GET"])
def get_customer_accounts(customer_id):
    amount_greater_than = request.args.get("amountGreaterThan")
    amount_less_than = request.args.get("amountLessThan")
    try:
        customer_accounts = account_service.get_customer_accounts(customer_id, amount_less_than, amount_greater_than)
        return {f"customer id: {customer_id} accounts": customer_accounts}
    except CustomerNotFoundError as e:
        return {
                   "message": str(e)
               }, 404


# GET /customer/{customer_id}/account/{account_id}: Get account with id of Y belonging to customer with id of X
# (if customer and account exist AND if account belongs to customer)
@account_ctrl.route("/customer/<customer_id>/account/<account_id>", methods=["GET"])
def get_account_by_id(customer_id, account_id):
    try:
        customer_account = account_service.get_account_by_id(customer_id, account_id)
        return customer_account.to_dict()
    except (CustomerNotFoundError, AccountNotFoundError) as e:
        return {
                   "message": str(e)
               }, 404


# PUT /customer/{customer_id}/account/{account_id}: Update account with id of Y belonging to customer with id of X
# (if customer and account exist AND if account belongs to customer)
@account_ctrl.route("/customer/<customer_id>/account/<account_id>", methods=["PUT"])
def update_account_by_id(customer_id, account_id):
    try:
        data = request.get_json()
        updated_account = account_service.update_account_by_id(customer_id, account_id, data)
        return updated_account.to_dict()
    except (CustomerNotFoundError, AccountNotFoundError) as e:
        return {
                   "message": str(e)
               }, 404
    except InvalidParameterError as e:
        return {
                   "message": str(e)
               }, 400


# DELETE /customer/{customer_id}/account/{account_id}: Delete account with id of Y belonging to customer with id of X
# (if customer and account exist AND if account belongs to customer)
@account_ctrl.route("/customer/<customer_id>/account/<account_id>", methods=["DELETE"])
def delete_account_by_id(customer_id, account_id):
    try:
        account_service.delete_account_by_id(customer_id, account_id)
        return {
            "message": f"account with id of {account_id} for customer with id of {customer_id} was deleted successfully"
        }
    except (CustomerNotFoundError, AccountNotFoundError) as e:
        return {
                   "message": str(e)
               }, 404

