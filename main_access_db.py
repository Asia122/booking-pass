import sqlite3
import hashlib
import argparse

from access_db import parse_args, save_new_username_correct, check_for_username_correct, print_all_users

with sqlite3.connect("db_password.db")as conn: 
    cursor = conn.cursor()
    
args = parse_args()

if args.c and args.p:
    ex = check_for_username_correct(args.c, args.p) # check if the username is present, the password is correct and get the role

    if ex is not None:
        u_role = ex.fetchall()[0][0]
        if u_role == "admin":
            print ("You are an admin, being an admin you can add new users to the database")
            choice = input("Do you want to add a new user? Type y or n")
            
            if choice == "y":
                n = input("Tell me the username: ")
                p = input("Tell me the password: ")
                r = input("Tell me the role (admin, doctor or restaurant): ")
                if r == "admin" or r == "doctor" or r == "restaurant":
                    save_new_username_correct(n, p, r) # use the function save_new_username_correct to insert a new user in the database
                else:
                    print ("Role not valid")

            elif choice == "n":
                print("Goodbye")

            else:
                print("Choice is not valid")
        
        elif u_role == "doctor":
            print("Now you can add new vaccinations...")
        
        elif u_role == "restaurant":
            print("You can check the green pass")
        
        else:
            print("There is a problem")
    

#if args.a and args.p and args.r:
#    save_new_username_correct(args.a, args.p, args.r)
#elif args.c and args.p:
#    ex = check_for_username_correct(args.c, args.p)
#    a = ex.fetchall()[0][0]
#    print ("The role is ", a)
#elif args.l:
#    print_all_users()

conn.close()


