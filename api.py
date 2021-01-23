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
    #all_challenges = {"challenges": challenges};
    return json.dumps(challenges)

@app.route('/tasks')
def tasks():
    """A tasks endpoint for obtaining a list of tasks"""
    print("Grabbing task data from database")
    conn = db.connect()
    tasks = db.get_tasks(conn) #tasks: json
    print(tasks)
    all_tasks = {"tasks": tasks}
    return all_tasks #to return a json named tasks

if __name__ == '__main__':
    app.run()