"""System module."""
import sqlite3

"""
The module visualize.py contains the functions used to visualize
data stored in the database password_db.db and in the dataset
people_vaccinated.csv.
"""


def print_all_users():
    """
    The function print_all_users gives the list of all the users
    present in the database and their role
    """

    # build the connection with the database
    with sqlite3.connect("db_password.db")as conn:
        cursor = conn.cursor()

    # get the username and the role from the table user_role
    rows = cursor.execute("SELECT username, role FROM user_role")
    conn.commit()

    # array containing all of the result set rows
    results = rows.fetchall()

    # print(results)
    print("Users:")
    for row in results:
        # for each row in result print the username and role
        print(row[0], row[1])

    # close the connection with the database
    conn.close()


def vaccinated_people(database):
    """
    This function allows to visualize the data contained
    in the file given as input
    """
    print("Now you can see by yourself if fiscal code is"
          "present in our database manually")

    # return the database
    return database


def print_info(answer, db_vaccine):
    """
    The function print_info takes as variables answer, which is
    the fiscal code, and db, the file where data are stored.
    This function give as output the date of the first vaccination shot
    """

    # print the fiscal code, name and surname of the person and
    # date of the first shot of vaccine
    list_fiscal_codes = db_vaccine["Fiscal Code"].tolist()
    if answer in list_fiscal_codes:
        print(db_vaccine["Fiscal Code"].loc[db_vaccine["Fiscal Code"]
              .str.lower() == answer.lower()].values[0],
              "is the fiscal code of",
              db_vaccine["Name"].loc[db_vaccine["Fiscal Code"]
              .str.lower() == answer.lower()].values[0],
              db_vaccine["Surname"].loc[db_vaccine["Fiscal Code"]
              .str.lower() == answer.lower()].values[0],
              "whose first dose date is",
              db_vaccine["Date First Shot"].loc[db_vaccine["Fiscal Code"]
              .str.lower() == answer.lower()].values[0])

    else:
        print("Fiscal Code not present in the database or format is invalid")
