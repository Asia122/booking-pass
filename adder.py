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

from csv import writer
import datetime
from datetime import datetime
from checker import check_fiscalcode
from fiscal_code import fiscal_code_calculator
from booking import select_date


def add_element(nperson, dataset):

    if check_fiscalcode(nperson):
        print(
            "sorry, but "
            + nperson
            + " fiscal code is already present "
            + "in the database, no reason to add again, thank you"
        )

    else:
        name = input("Please enter the name -> ")
        while name == "":
            name = input(
                "You can't enter nothing... " + "so please... put the name -> "
            )

        surname = input("Please enter the surname -> ")
        while surname == "":
            surname = input(
                "You can't enter nothing... " + "so please... the surname -> "
            )

        gender = input("Please enter your gender: M or F -> ")
        while gender == "":
            gender = input(
                "You can't enter nothing... " + "so please... the gender: M or F -> "
            )

        birthday = input("Please enter the birthday gg/mm/yyyy-> ")
        while birthday == "":
            birthday = input(
                "You can't enter nothing... "
                + "so please... put the birthday gg/mm/yyyy-> "
            )

        birthplace = input("Please enter the birth place -> ")
        while birthplace == "":
            birthplace = input(
                "You can't enter nothing... " + "so please... put the birth place -> "
            )

        fiscalcode = fiscal_code_calculator(name, surname, birthday, gender, birthplace)

        if check_fiscalcode(fiscalcode):
            print(
                "sorry, but "
                + fiscalcode
                + " fiscal code is already present "
                + "in the database, no reason to add again, thank you"
            )

        else:
            # ask to the patient if he/she is alre
            already_vaccinated = input(
                "Have you already received the first " + "vaccine shot? Type y or n: "
            )

            if already_vaccinated == "y":
                # check if the date was inserted in the correct format
                check_format = False

                while not check_format:
                    # get the day of the first dose
                    firstdose = input(
                        "Enter the date of the vaccination in "
                        + "the format gg/mm/yyyy"
                    )
                    try:
                        datetime.strptime(firstdose, "%d/%m/%Y")
                        check_format = True
                    except ValueError:
                        check_format = False
                        print("Incorrect date format")

            else:
                firstdose = select_date()

            # Open file in append mode
            with open("people_vaccinated.csv", "a") as peopledata:
                # Create a writer object from csv module
                csv_writer = writer(peopledata)
                # Add contents of list as last row in the csv file
                csv_writer.writerow(
                    [fiscalcode, name, surname, gender, birthday, birthplace, firstdose]
                )

            print("You succeffully registered", name, surname, "'s vaccination date!")
