"""
The adder module has a single
function with the purpose
of let doctors appending inside the dataset
the personal information and date of vaccination 
of new people.

The input will be checked to
see if it is already inside the database.

It is necessary for the user to
input a string that is not empty."
"""

import csv
import pandas as pd
from checker import Check
from fiscal_code import fiscal_code_calculator
from booking import select_date

def add_element(nperson, response=""):
    db = pd.DataFrame(pd.read_csv('people_vaccinated.csv'))
    
    if Check().check_fiscalcode(nperson):
        return print("sorry, but " + nperson + " fiscal code is already present " +
                     "in the database, no reason to add again, thank you")

    else:
        name = input("Please enter the name -> ")
        while(name == ""):
            name = input("You can't enter nothing... " +
                          "so please... put the name -> ")
            
        surname = input("Please enter the surname -> ")
        while(surname == ""):
            surname = input("You can't enter nothing... " +
                            "so please... the surname -> ")
            
        gender = input("Please enter your gender: M or F -> ")
        while(gender == ""):
            gender = input("You can't enter nothing... " +
                            "so please... the gender: M or F -> ")
            
        birthday = input("Please enter the birthday gg/mm/yyyy-> ")
        while(birthday == ""):
            birthday = input("You can't enter nothing... " +
                            "so please... put the birthday gg/mm/yyyy-> ")
            
        birthplace = input("Please enter the birth place -> ")
        while(birthplace == ""):
            birthplace = input("You can't enter nothing... " +
                            "so please... put the birth place -> ")

        """= input("Please enter the firt dose date gg/mm/yyyy -> ")
        while(firstdose == ""):
            firstdose = input("You can't enter nothing... " +
                            "so please... put the firt dose date -> ")"""
            
        fiscalcode = fiscal_code_calculator(name, surname, birthday, gender, birthplace)

        if Check().check_fiscalcode(fiscalcode):
            return print("sorry, but " + fiscalcode + " fiscal code is already present " +
                         "in the database, no reason to add again, thank you")
        
        firstdose = select_date()
                   
        with open('people_vaccinated.csv', 'a') as peopledata:
            newpeopledata = csv.writer(peopledata)
            row = len(db)
            newpeopledata.writerow([fiscalcode, name, surname, gender, birthday, birthplace, firstdose])
        
        return print("You succeffully registered",name, surname,"'s vaccination date!")


    
    
    
        
