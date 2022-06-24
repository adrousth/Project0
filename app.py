from flask import Flask
from controller.controller import ctrl


if __name__ == 'main':
    app = Flask(__name__)
    app.register_blueprint(ctrl)
    app.run(port=8080, debug=True)
