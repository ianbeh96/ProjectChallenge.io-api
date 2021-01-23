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
    print("Grabbing user data from database")
    conn = db.connect()
    users = db.get_users(conn) #users: dict
    return json.dumps(users)
    
@app.route('/challenges')
def challenges():
    """A challenges endpoint for obtaining a list of challenges"""
    print("Grabbing challenge data from database")
    conn = db.connect()
    challenges = db.get_challenges(conn) #challenges: dict
    return json.dumps(challenges)

if __name__ == '__main__':
    app.run()