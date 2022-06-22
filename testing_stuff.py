from flask import Flask, request

from faker import Faker

fake = Faker()

app = Flask(__name__)
users = {
    10001: {
        "first name": "joe",
        "last name": "smith"
    },
    10002: {
        "first name": "steve",
        "last name": "johnson"
    }

}


@app.route('/users', methods=['GET'])
def get_users():
    return users


@app.route('/users', methods=['POST'])
def add_user():
    print("add user")
    data = request.get_json()
    print(data)
    return {}


app.run(port=8081)
