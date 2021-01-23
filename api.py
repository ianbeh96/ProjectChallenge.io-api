import db
import json

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/health')
def health():
    return 'Ok =)'

@app.route('/users')
def users():
    print("grabbing data from database")
    conn = db.connect()
    users = db.get_users(conn) #users: dict
    abc = {
        "name": "John",
        "age": 30,
        "married": True,
        "divorced": False}
    return json.dumps(user)
    

if __name__ == '__main__':
    app.run()