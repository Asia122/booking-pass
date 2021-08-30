
"WRITE THE PROGRAM DESCRIPTION"
#LAVORIAMO QUI

import calendar
import datetime
from datetime import datetime
from datetime import date
import argparse
import pandas as pd
from adder import add_element
from checker import Check
import sqlite3
import hashlib
import argparse
from access_db import parse_args, save_new_username_correct, check_for_username_correct
from fiscal_code import fiscal_code_calculator
from visualize import print_all_users, vaccinated_people, print_info


args = parse_args()
db = pd.DataFrame(pd.read_csv('people_vaccinated.csv'))

if args.l:
    ex = check_for_username_correct(args.c, args.p) # check if the username is present and the password iserted is correct

    if ex is not None:
        u_role = ex.fetchall()[0][0] #get the role
        
        if u_role == "admin":# check if the role is equal to admin
            print_all_users()

        else:
            print("You aren't an admin, you can't visualize the list of users")
    

elif args.d:
    ex = check_for_username_correct(args.c, args.p) # check if the username is present,
    #the password is correct and get the role

    if ex is not None:
        u_role = ex.fetchall()[0][0] #get the role
        
        if u_role == "doctor":# check if the role is equal to doctor
            table = vaccinated_people(db)
            print (table)

        else:
            print("You aren't a doctor, you can't visualize the list of vaccinated people")
    

elif args.f:
    ex = check_for_username_correct(args.c, args.p) # check if the username is present,
    #the password is correct and get the role

    if ex is not None:
        u_role = ex.fetchall()[0][0] #get the role
        
        if u_role == "doctor":# check if the role is equal to doctor
            input_answer = input("Insert the Fiscal Code:")
            print_info(input_answer, db)

        else:
            print("You aren't a doctor, you can't visualize the personal informations of the patients")

else:
    ex = check_for_username_correct(args.c, args.p) # check if the username is present,
    #the password is correct and get the role

    if ex is not None:
        u_role = ex.fetchall()[0][0] #get the role
        if u_role == "admin":
            print ("You are an admin, being an admin you can add new users to the database or modify an old one")
            choice = input("Do you want to add a new user? Type y or n: ")
            
            if choice == "y":
                n = input("Tell me the username: ")
                p = input("Tell me the password: ")
                r = input("Tell me the role (admin, doctor or restaurant): ")
                if r == "admin" or r == "doctor" or r == "restaurant":
                    save_new_username_correct(n, p, r) # use the function save_new_username_correct
                    #to insert a new user in the database or modify an old one
                else:
                    print ("Role not valid")

            elif choice == "n":
                print("Goodbye")

            else:
                print("Choice is not valid")
        
        elif u_role == "doctor":
            print("Now you can add new vaccinations")#OOOOooooooOOOOOOoooOOoOo python main.py -c RickyTrabu -p Wudy
            answer = input("Introduce the Fiscal Code or simply push enter if you want it calculated automatically ")
            add_element(answer)
        
        elif u_role == "restaurant":   #python main.py -c AndreaRocco -p DataAnalyticsMaster
            nperson = input("Check if a person has the greenpass giving his/her Fiscal Code:  ")
            Check().CheckGreenPass(nperson)
        
        else:
            print("There is a problem")
    else:
        print("User is not present, or password is invalid")