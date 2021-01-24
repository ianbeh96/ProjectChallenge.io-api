import db_config as config 
import psycopg2

from typing import List

def connect():
    """Initiate a postgres database connection using psycopg2

    Returns:
    A psycopg2.extensions.connection object
    """
    return psycopg2.connect(
        dbname = config.dbname,
        user = config.dbuser,
        password = config.dbpassword,
        host = config.dbhost,
        port = '5432'
    )

def get_users(conn) -> List[dict]:
    """Grab a list of users from the database.
    conn: psycopg2.extensions.connection object

    Returns:
    A list of python dicts containing user data
    """
    users = []
    curr = conn.cursor()
    curr.execute('SELECT * FROM users;')
    for row in curr.fetchall():
        users.append(db_row_to_dict_user(row))
    return users

def db_row_to_dict_user(row: tuple) -> dict:
    """Helper function to convert a tuple of data into a dict
    row: tuple of user data

    Returns:
    A dict with db columns as the dict keys
    """
    column_names = [
            "id", "username", "password", "name", 
            "email", "challenge_id", "points", "role"
        ]
    return dict(zip(column_names, list(row)))

def get_challenges(conn) -> List[dict]:
    """Grab a list of challenges from the database.
    conn: psycopg2.extensions.connection object

    Returns:
    A list of python dicts containing challenge data
    """
    challenges = []
    curr = conn.cursor()
    curr.execute('SELECT * FROM challenges;')
    for row in curr.fetchall():
        challenges.append(db_row_to_dict_challenge(row))
    return challenges

def db_row_to_dict_challenge(row: tuple) -> dict:
    """Helper function to convert a tuple of data into a dict
    row: tuple of challenge data

    Returns:
    A dict with db columns as the dict keys
    """
    column_names = [
            "id", "challenge_id", "name", "status", 
            "leader", "start_date", "end_date"
        ]
    return dict(zip(column_names, list(row)))

def get_tasks(conn) -> List[dict]:
    """Grab a list of tasks from the database.
    conn: psycopg2.extensions.connection object
    Returns:
    A list of python dicts containing task data
    """
    tasks = []
    curr = conn.cursor()
    curr.execute('SELECT * FROM tasks;')
    for row in curr.fetchall():
        tasks.append(db_row_to_dict_task(row))
    return tasks

def db_row_to_dict_task(row: tuple) -> dict:
    """Helper function to convert a tuple of data into a dict
    row: tuple of task data

    Returns:
    A dict with db columns as the dict keys
    """
    column_names = [
            "id", "task_id", "challenge_id", "name", "owner", 
            "status", "points"
        ]
    return dict(zip(column_names, list(row)))

def get_user(conn, username) -> List[dict]:
    """Grab a single user from the database.
    conn: psycopg2.extensions.connection object
    Returns:
    A list of python dicts containing THE user data
    """
    user = []
    curr = conn.cursor()
    curr.execute("SELECT username, name, email, points, role FROM users WHERE username='" + username + "';")
    for row in curr.fetchall():
        user.append(db_row_to_dict_single_user(row))
    return user

def db_row_to_dict_single_user(row: tuple) -> dict:
    """Helper function to convert a tuple of data into a dict
    row: tuple of user data

    Returns:
    A dict with db columns as the dict keys
    """
    column_names = [
            "username", "name", "email", "points", "role"
        ]
    return dict(zip(column_names, list(row)))