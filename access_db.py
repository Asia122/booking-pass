"""System module."""
import sqlite3
import hashlib
import argparse

"""
The module access_db.py contains the functions used to access to the database
db_password.db and modify it.
It also contains the function parse_args which defines the arguments needed
to perform the operations inside the program.
"""


def parse_args():
    """
    The function parse_args will take the arguments you provide on
    the command line when you run your program and interpret them according
    to the arguments you have added to your ArgumentParser object.
    """
    parser = argparse.ArgumentParser()

    # add the argument p which takes the password as input,
    # which is always required
    parser.add_argument('-p', help="the username password",
                        required=True)

    # add the argument c which takes the username as input,
    # which is always required
    parser.add_argument('-c', help="check username and password, return role"
                        "(requires -p)", required=True)

    # add the argument l which allows to get the list of all users
    parser.add_argument('-l', help="list all users requires -c and -p",
                        action='store_true', required=False)

    # add the argument d which allows to get the list of all vaccinated people
    parser.add_argument('-d', help="list vaccinated people requires -c and -p",
                        action='store_true', required=False)

    # add the argument d which allows to get the personal info
    # of vaccinated people
    parser.add_argument('-f', help="personal information requires -c and -p",
                        action='store_true', required=False)

    return parser.parse_args()


def check_for_username_correct(username, password):
    """
    This function takes as input username and password and returns the role
    of the user.
    It checks if the username is present in the database and the connected
    password is correct.
    """
    # build connection with the database
    with sqlite3.connect("db_password.db")as conn:
        cursor = conn.cursor()

    # compute hash of password to check it
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # prepared statement
    rows = cursor.execute("SELECT * FROM user WHERE username=? and password=?",
                          (username, digest))
    conn.commit()
    results = rows.fetchall()

    # check if the search given results and assign the role to the variable
    if results:
        r_role = cursor.execute("SELECT role FROM user_role WHERE username=?",
                           (results[0][0],))
        role = r_role.fetchall()[0][0]

    else:
        role = 0

    # return the role of the user
    return role


def save_new_username_correct(username, password, role):
    """
    This function takes as input username, password and role of the user.
    It allows to add a new user to the database or modify a user which is
    aleady present in the database.
    """

    # build connection with the database
    with sqlite3.connect("db_password.db")as conn:
        cursor = conn.cursor()

    # compute hash of the password and store it in db
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # prepared statements to avoid sql injection
    cursor.execute("INSERT OR REPLACE INTO user VALUES (?,?)",
                   (username, digest))
    cursor.execute("INSERT OR REPLACE INTO user_role VALUES (?,?)",
                   (username, role))
    conn.commit()

    # close the connection with the database
    conn.close()
