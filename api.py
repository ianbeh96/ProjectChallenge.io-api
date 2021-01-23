import db
import json

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    """A base endpoint just because"""
    return 'Hello World!'

@app.route('/health')
def health():
    """A health endpoint for checking server uptime"""
    return 'Ok =)'

@app.route('/users')
def users():
    """A users endpoint for obtaining a list of users"""
    print("Grabbing data from database")
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