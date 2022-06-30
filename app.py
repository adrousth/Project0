from flask import Flask
from controller.controller import ctrl

# print(__name__)
if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(ctrl)
    app.run(port=8080, debug=True)
