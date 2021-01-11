import db

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
    return str(users)
    

if __name__ == '__main__':
    app.run()