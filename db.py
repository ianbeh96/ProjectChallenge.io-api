import db_config as config 
from typing import List
import psycopg2 

def connect():
    return psycopg2.connect(
        dbname = config.dbname,
        user = config.dbuser,
        password = config.dbpassword,
        host = config.dbhost,
        port = '5432'
    )

def get_users(conn) -> List[dict]:
    users = []
    curr = conn.cursor()
    curr.execute('SELECT * FROM users;')
    for row in curr.fetchall():
        users.append(db_to_dict(row))
    return users

def db_to_dict(row: tuple):
    column_names = [
            "id", "username", "password", "name", 
            "email", "challenge_id", "points", "role"
        ]
    return dict(zip(column_names, list(row)))