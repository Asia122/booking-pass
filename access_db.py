"""
The module access_db.py contains the functions used to access to the database
db_password.db and modify it.
It also contains the function parse_args which defines the arguments needed
to perform the operations inside the program.
"""
import sqlite3
import hashlib
import argparse


def parse_args():
    """
    The function parse_args will take the arguments you provide on
    the command line when you run your program and interpret them according
    to the arguments you have added to your ArgumentParser object.
    """

    parser = argparse.ArgumentParser(description='This program will' +
                                     ' check if the username and ' +
                                     'password given as input ' +
                                     'are registered inside our ' +
                                     'user database and, depending on ' +
                                     'the role (admin, doctor or ' +
                                     'restaurant), it will allow to ' +
                                     'access to different sections' +
                                     'of the program. Username and ' +
                                     'password are mandatory' +
                                     'so please insert both of them' +
                                     ' separated by a space ')

    group = parser.add_mutually_exclusive_group()

    parser.add_argument("username", help="the username")
    parser.add_argument("password", help="the password of the user")

    # add the argument l which allows to get the list of all users
    group.add_argument('-l', help='shows the list all users,' +
                       ' you need to be an admin to access',
                       action='store_true', required=False)

    # add the argument d which allows to get the list of all vaccinated people
    group.add_argument('-d', help='shows the list of vaccinated people, ' +
                       'you need to be a doctor to access',
                       action='store_true', required=False)

    # add the argument f which allows to get the personal info
    # of vaccinated people
    group.add_argument('-f', help="shows the personal information " +
                        ' of patients you need to be a doctor to access',
                        action='store_true', required=False)

    args = parser.parse_args()
    username = args.username
    password = args.password

    return args, username, password


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
