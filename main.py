"""System module."""
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

args = parse_args()
db = pd.DataFrame(pd.read_csv("people_vaccinated.csv"))

if args.l:
    # check if the username is present and the passwordis correct
    # using the imported function check_for_username_correct
    # if there is no match the function returns 0
    ex = check_for_username_correct(args.c, args.p)

    if ex != 0:
        u_role = ex.fetchall()[0][0]  # get the role

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
    ex = check_for_username_correct(args.c, args.p)

    if ex != 0:
        u_role = ex.fetchall()[0][0]  # get the role

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
    ex = check_for_username_correct(args.c, args.p)

    if ex != 0:
        u_role = ex.fetchall()[0][0]  # get the role

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
    ex = check_for_username_correct(args.c, args.p)

    if ex != 0:
        u_role = ex.fetchall()[0][0]  # get the role
        if u_role == "admin":
            print(
                "You are an admin so you can add new users to the database" +
                " or modify an old one"
            )
            choice = input("Do you want to add a new user? Type y or n: ")

            if choice == "y":
                n = input("Tell me the username: ")
                p = input("Tell me the password: ")
                r = input("Tell me the role (admin, doctor or restaurant): ")
                if r in ["admin", "doctor", "restaurant"]:
                    save_new_username_correct(
                        n, p, r
                    )  # use the function save_new_username_correct
                    # to insert a new user in the database or modify an old one
                else:
                    print("Role not valid")

            elif choice == "n":
                print("You can only add new users in this section," +
                      " if you want to do something else try -l," +
                      " -c username -p password")

            else:
                print("Choice is not valid")

        elif u_role == "doctor":
            print("Now you can add new vaccinations")
            answer = input(
                "Introduce the Fiscal Code or simply push enter if" +
                "you want it to be calculated "
            )

            # call the function add_element which allows to add a new patient
            # to the dataset given the fiscal code and the database
            add_element(answer, db)

        elif u_role == "restaurant":
            # python main.py -c AndreaRocco -p DataAnalyticsMaster
            nperson = input("Check if a person has the greenpass" +
                            "giving the Fiscal Code: ")

            # call the function check_green_pass which given the
            # fiscal code tells if the person has the greenpass or not
            check_green_pass(nperson)

        else:
            print("There is a problem")
    else:
        print("User is not present, or password is invalid")
