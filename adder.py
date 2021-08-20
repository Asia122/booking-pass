"""
The adder module has a single
function with the purpose
of let doctors appending inside the dataset
the personal information and date of vaccination 
of new people

The input will be checked to
see if it is already inside the
database.


It is necessary for the user to
input a string that is not empty."
"""

import csv
import pandas as pd
from checker import Check


def add_element(nperson, response=""):

    """
    This function comes into play once the user inputs a new perons 
    is not inside the database, or when, after
    the input, the user writes the optional argument -a
    and proceeds to add the personal information and vaccination date.
    """
    db = pd.DataFrame(pd.read_csv('people_vaccinated.csv'))
    if Check().check_fiscalcode(nperson):
        return print("sorry, but " + nperson + " fiscal code is already present " +
                     "in the database, no reason to add again, thank you")

    else:
        name = input("Please enter the name -> ")
        while(name == ""):
            name = input("You can't enter nothing... " +
                          "so please... put anything -> ")
        surname = input("Please enter the surname -> ")
        while(surname == ""):
            surname = input("You can't enter nothing... " +
                            "so please... put anything -> ")
        birthday = input("Please enter the birthday -> ")
        while(birthday == ""):
            birthday = input("You can't enter nothing... " +
                            "so please... put anything -> ")   
        birthplace = input("Please enter the birth date gg/mm/yyyy -> ")
        while(birthplace == ""):
            birthplace = input("You can't enter nothing... " +
                            "so please... put anything -> ")
        firstdose = input("Please enter the firt dose date gg/mm/yyyy -> ")
        while(firstdose == ""):
            firstdose = input("You can't enter nothing... " +
                            "so please... put anything -> ") 
                    
        with open('people_vaccinated.csv', 'a') as peopledata:
            newpeopledata = csv.writer(peopledata)
            row = len(db)
            peopledata.write("\n")
            newpeopledata.writerow([row,nperson, name, surname, birthday, birthplace, firstdose])
        return print("Thank you for your contribution!")
        
