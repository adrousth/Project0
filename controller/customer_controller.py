from exception.exceptions import *

from flask import request, Blueprint
from model.customer import Customer
from service.customer_service import CustomerService

customer_ctrl = Blueprint('customer_controller', __name__)
customer_service = CustomerService()


# POST /customers: Creates a new customer
@customer_ctrl.route("/customers", methods=["POST"])
def add_customer():
    data = request.get_json()
    try:
        customer = customer_service.add_customer(data)
        return customer.to_dict(), 202
    except InvalidParameterError as e:
        return {
            "message": str(e)
        }, 400


# GET /customers: Gets all customers
@customer_ctrl.route("/customers", methods=["GET"])
def get_all_customers():
    customers = customer_service.get_all_customers()
    return {"customers": customers}


# GET /customer/{customer_id}: Get customer with an id of X (if the customer exists)
@customer_ctrl.route("/customer/<customer_id>", methods=["GET"])
def get_customer_by_id(customer_id):
    print("get customer by id:", customer_id)
    try:
        customer = customer_service.get_customer_by_id(customer_id)
        return customer.to_dict()
    except CustomerNotFoundError as e:
        return {
                   "message": str(e)
               }, 404


# PUT /customer/{customer_id}: Update customer with an id of X (if the customer exists)
@customer_ctrl.route("/customer/<customer_id>", methods=["PUT"])
def update_customer_by_id(customer_id):
    print("update customer by id:", customer_id)
    try:
        data = request.get_json()
        return customer_service.update_customer(customer_id, data).to_dict()
    except CustomerNotFoundError as e:
        return {
                   "message": str(e)
               }, 404
    except InvalidParameterError as e:
        return {
                   "message": str(e)
               }, 400


# DELETE /customer/{customer_id}: Delete customer with an id of X (if the customer exists)
@customer_ctrl.route("/customer/<customer_id>", methods=["DELETE"])
def delete_customer_by_id(customer_id):
    print("delete customer by id:", customer_id)
    try:
        customer_service.delete_customer_by_id(customer_id)
        return {
            "message": f"customer with id of {customer_id} was deleted successfully, along with all related accounts"
        }
    except CustomerNotFoundError as e:
        return {
                   "message": str(e)
               }, 404

