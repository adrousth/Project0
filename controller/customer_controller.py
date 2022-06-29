from exception.exceptions import *

from flask import request, Blueprint
from model.customer import Customer
from service.customer_service import CustomerService

customer_ctrl = Blueprint('controller', __name__)
customer_service = CustomerService()


# POST /customers: Creates a new customer
@customer_ctrl.route("/customers", methods=["POST"])
def add_customer():
    print("add customer")
    data = request.get_json()
    customer_service.add_customer(data)
    return {}


# GET /customers: Gets all customers

@customer_ctrl.route("/customers", methods=["GET"])
def get_all_customers():
    print("get all customers")
    return customer_service.get_all_customers()


# GET /customer/{customer_id}: Get customer with an id of X (if the customer exists)
@customer_ctrl.route("/customer/<customer_id>", methods=["GET"])
def get_customer_by_id(customer_id):
    print("get customer by id:", customer_id)
    try:
        return customer_service.get_user_by_id(customer_id)  # dictionary
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
        print(data)
        return customer_service.update_customer(Customer(customer_id, data['first_name'], data['last_name']))
    except CustomerNotFoundError as e:
        return {
                   "message": str(e)
               }, 404


# DELETE /customer/{customer_id}: Delete customer with an id of X (if the customer exists)
@customer_ctrl.route("/customer/<customer_id>", methods=["DELETE"])
def delete_customer_by_id(customer_id):
    print("delete customer by id:", customer_id)
    try:
        return customer_service.delete_customer_by_id(customer_id)
    except CustomerNotFoundError as e:
        return {
                   "message": str(e)
               }, 404