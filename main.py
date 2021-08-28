
"WRITE THE PROGRAM DESCRIPTION"
#LAVORIAMO QUI


import argparse
import pandas as pd
from adder import add_element
from checker import Check
import sqlite3
import hashlib
import argparse
from access_db import parse_args, save_new_username_correct, check_for_username_correct, print_all_users
args = parse_args()
db = pd.DataFrame(pd.read_csv('people_vaccinated.csv'))


if args.c and args.p:
    ex = check_for_username_correct(args.c, args.p) # check if the username is present,
    #the password is correct and get the role

    if ex is not None:
        u_role = ex.fetchall()[0][0]
        if u_role == "admin":
            print ("You are an admin, being an admin you can add new users to the database")
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
            print("Now you can add new vaccinations...")#OOOOooooooOOOOOOoooOOoOo
            answer = input("Introduce the Fiscal Code or simply push enter if you want it calculated automatically ")
            add_element(answer)
            
        
        elif u_role == "restaurant":
            print("You can check the green pass")
        
        else:
            print("There is a problem")
    else:
        print("User is not present, or password is invalid")
    
elif args.l:
    print_all_users()

else:
    print ("Argument is not valid")












#__---_--___---__--____-__-_--__----________---_----_-_-_-_-_-_-__-_-_-_-_--_-_-_-_-_-_-_-_-_-_-_-_-

parser = argparse.ArgumentParser(description='This program will' +
                                             ' check if the given personal information are correct' +
                                             ' write in a dataset the date of your vaccination ' +
                                             ' check if in a given date you will have the green pass ')
#la descrizione va fatta meglio
group = parser.add_mutually_exclusive_group()
parser.add_argument("name", help="input the fiscal code of a person")

# -d per far uscire tutto il dataset
group.add_argument("-d", "--database", action="store_true",
                   help="add a new person")


args = parser.parse_args()
answer = args.name

if args.database:
    print("Now you can see by yourself if " +
          answer + " fiscal code is present in our database manually")
    print(db)
        
else:
    print(db["Fiscal Code"].loc[db["Fiscal Code"].str.lower() == answer.lower()].values[0], "is the fiscal code of",
    db["Name"].loc[db["Fiscal Code"].str.lower() == answer.lower()].values[0],
    db["Surname"].loc[db["Fiscal Code"].str.lower() ==
    answer.lower()].values[0], "whose first dose date is on",
    db["Date First Shot"].loc[db["Fiscal Code"].str.lower() ==
    answer.lower()].values[0])



