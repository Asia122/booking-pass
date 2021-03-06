"""Once the username and a password are given,the software
check if the username is present and the password inserted
in is the corresponding one, if everything is correct  the
program allows users to access different sections based on
their role.

Username, password and roles are registered in
the database access_db.db. Only users whose role is admin
can modify the access_db.db adding new users or modify the
password or the role of the existing ones.

Moreover he/she can visualize the list of all users.
"""
import pandas as pd
from access_db import parse_args, save_new_username_correct
from access_db import check_for_username_correct
from visualize import print_all_users, vaccinated_people, print_info
from adder import add_element
from checker import check_green_pass

"""
This module recalls the functions present in the other modules
to make them work together in an organic way and improve
the user experience.
"""

# assign the values returned by the function parse_args()
# to a variable
arguments = parse_args()

# assign the arguments
args = arguments[0]

# get the username
username = arguments[1]

# get the password
password = arguments[2]

db = pd.DataFrame(pd.read_csv("people_vaccinated.csv"))

if args.l:
    # check if the username is present and the passwordis correct
    # using the imported function check_for_username_correct
    # if there is no match the function returns 0
    u_role = check_for_username_correct(username, password)

    if u_role != 0:

        if u_role == "admin":  # check if the role is equal to admin
            print_all_users()

        else:
            print("You aren't an admin, you can't visualize the list of users")
    else:
        print("User is not present, or password is invalid")

elif args.d:
    # check if the username is present, the password is correct
    # using the imported function check_for_username_correct
    # if there is no match the function returns 0
    u_role = check_for_username_correct(username, password)

    if u_role != 0:

        if u_role == "doctor":  # check if the role is equal to doctor
            table = vaccinated_people(db)
            print(table)

        else:
            print(
                "You aren't a doctor, you can't visualize the list" +
                " of vaccinated people"
            )

    else:
        print("User is not present, or password is invalid")


elif args.f:
    # check if the username is present, the password is correct
    # using the imported function check_for_username_correct
    # if there is no match the function returns 0
    u_role = check_for_username_correct(username, password)

    if u_role != 0:

        if u_role == "doctor":  # check if the role is equal to doctor
            input_answer = input("Insert the Fiscal Code:")
            print_info(input_answer, db)

        else:
            print(
                "You aren't a doctor, you can't visualize the" +
                " personal information of the patients"
            )
    else:
        print("User is not present, or password is invalid")


else:
    # check if the username is present, the password is correct
    # using the imported function check_for_username_correct
    # if there is no match the function returns 0
    u_role = check_for_username_correct(username, password)

    if u_role != 0:

        if u_role == "admin":
            print(
                "You are an admin so you can add new users to the database" +
                " or modify an old one"
            )
            choice = input("Do you want to add a new user? Type y or n: ")

            if choice == "y":
                n = input("Tell me the username: ")

                while len(n) == 0:
                    n = input("ERROR - Tell me the username: ")

                p = input("Tell me the password: ")

                while len(p) == 0:
                    p = input("ERROR - Tell me the password: ")

                right_role = False
                r = input("Tell me the role (admin, doctor or restaurant): ")

                while not right_role:
                    if r in ["admin", "doctor", "restaurant"]:
                        save_new_username_correct(
                            n, p, r
                        )  # use the function save_new_username_correct
                        # to insert a new user in the database or modify an old one
                        right_role = True
                    else:
                        print("Role not valid")
                        r = input("ERROR - Tell me the role (admin, doctor or restaurant): ")

            elif choice == "n":
                print("You can only add new users in this section," +
                      " if you want to do something else try -l")

            else:
                print("Choice is not valid")

        elif u_role == "doctor":
            print("Now you can add new vaccinations")
            answer = input(
                "Introduce the Fiscal Code or simply push enter if" +
                " you want it to be calculated "
            )

            # call the function add_element which allows to add a new patient
            # to the dataset given the fiscal code and the database
            add_element(answer)

        elif u_role == "restaurant":

            nperson = input("Check if a person has the greenpass" +
                            "giving the Fiscal Code: ")

            # call the function check_green_pass which given the
            # fiscal code tells if the person has the greenpass or not
            print(check_green_pass(nperson))

        else:
            print("There is a problem")
    else:
        print("User is not present, or password is invalid")
