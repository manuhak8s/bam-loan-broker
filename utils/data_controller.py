""" import os, sys, sqlite3, uuid, time, random
from termcolor import colored

db_filepath = 'data/users.db'
connection = sqlite3.connect(db_filepath)
cursor = connection.cursor()

# Existenz feststellen
def init_user_db():
    print(colored("initializing database ...", 'yellow'))
    try:
        if (os.path.exists(db_filepath) == False):
            print("creating database file to local project")
            f = open(db_filepath, "w")
        else:
            print(colored("DB file already exists in local project", 'blue'))  
    except:
        print(colored("error while initializing database", 'red'))  

def create_users_table():
    sql = "CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
    cursor.execute(sql)

def generate_user_id():
    return random.randrange(10000)

def insert_user(username, password):
    print(colored('inserting user to database ...'))
    try:
        sql = "INSERT INTO users VALUES(?, ?, ?)"
        cursor.execute(sql, (generate_user_id(), username, password))
        connection.commit()
        print(colored('inserting user to database succeeded', 'green'))
    except:
        print(colored('error while inserting user to database', 'red'))

def get_user(username, password):
    print(colored('selecting user from database ...', 'yellow'))
    try:
        sql = "SELECT * FROM users WHERE username LIKE ? AND password Like ?"
        cursor.execute(sql, (username, password))
        return cursor.fetchall()
    except:
        print(colored('error while selecting user from database', 'red'))

def validate_get_user_query(list):
    if len(list) == 0 or len(list) > 1:
        return False
    else:
        return True

def recreate_database(path):
    print(colored("recreating database ...", 'yellow'))
    try:
        print("delete database")
        os.remove(path)
        print("initializing new database")
        init_user_db()
        print(colored('new database set up', 'green'))
    except:
        print("dropping database failed") """