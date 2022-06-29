from flask import Flask
from controller.account_controller import account_ctrl
from controller.customer_controller import customer_ctrl

if __name__ == 'main':
    app = Flask(__name__)
    app.register_blueprint(account_ctrl)
    app.register_blueprint(customer_ctrl)
    app.run(port=8080, debug=True)
