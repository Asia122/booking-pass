import sqlite3
import hashlib
import argparse
import pandas as pd


db = pd.DataFrame(pd.read_csv('people_vaccinated.csv'))

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
    parser.add_argument('-d', help="list vaccinated people", action='store_true',
                        required=False)
    parser.add_argument('-f', help="personal information", action='store_true',
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

    conn.close()


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

    conn.close()
    


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
    
    conn.close()

def vaccinated_people(db):
    print("Now you can see by yourself if fiscal code is present in our database manually")
    print(db)

def print_info(answer):
    print(db["Fiscal Code"].loc[db["Fiscal Code"].str.lower() == answer.lower()].values[0], "is the fiscal code of",
    db["Name"].loc[db["Fiscal Code"].str.lower() == answer.lower()].values[0],
    db["Surname"].loc[db["Fiscal Code"].str.lower() ==
    answer.lower()].values[0], "whose first dose date is on",
    db["Date First Shot"].loc[db["Fiscal Code"].str.lower() ==
    answer.lower()].values[0])



