import sqlite3
import hashlib
import argparse


# example of a simple password database with Python and SQLite.
#  - Prepared statements to avoid vulnerable SQL injection
#  - hashed passwords


# add a username
# python access_db.py -a RickyTrabu -p Wudy -r medico
# python access_db.py -a Nicole00 -p Lab2021 -r admin
# python access_db.py -a AndreaRocco -p DataAnalyticsMaster -r restaurant
# python access_db.py -a LeoProve -p ConquiQuarto -r medico

# check if it exists and its role
# python access_db.py -c Nicole00 -p Lab2021
# python access_db.py -c pippo -p differentpwd  # will not work!

with sqlite3.connect("db_password.db")as conn:
    cursor = conn.cursor()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help="add a usernamename (requires -p)",
                        required=False)
    parser.add_argument('-p', help="the username password",
                        required=True)
    parser.add_argument('-r', help="the username role",
                        required=False)
    parser.add_argument('-c', help="check for a usernamename and password and return role"
                                   "(requires -p)", required=False)
    parser.add_argument('-l', help="list all users", action='store_true',
                        required=False)
    return parser.parse_args()


def save_new_username_correct(username, password, role):
    with sqlite3.connect("db_password.db")as conn:
        cursor = conn.cursor()

    # compute hash of the password and store it in db
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # prepared statements to avoid sql injection
    cursor.execute("INSERT OR REPLACE INTO user VALUES (?,?,?)",
                   (username, digest, role))
    cursor.execute("INSERT OR REPLACE INTO user_role VALUES (?,?)",
                   (username, role))
    conn.commit()


def check_for_username_correct(username, password):
    with sqlite3.connect("db_password.db")as conn:
        cursor = conn.cursor()

    # compute hash of password to check it
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # prepared statement
    rows = cursor.execute("SELECT * FROM user WHERE username=? and password=?",
                          (username, digest))
    conn.commit()
    results = rows.fetchall()
    
    if results:
        b = cursor.execute("SELECT role FROM user_role WHERE username=?",
                           (results[0][0],))
        #return the role of the user
        return b
    else:
        print("User is not present, or password is invalid")


def print_all_users():
    with sqlite3.connect("db_password.db")as conn:
        cursor = conn.cursor()
    rows = cursor.execute("SELECT username FROM user")
    conn.commit()
    results = rows.fetchall()
    # print(results)

    print("Users:")
    for row in results:
        print(row[0])



