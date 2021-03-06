"""
The module adder.py has the purpose of let doctors append inside
the dataset people_vaccinated.csv the personal information of
new people.

Name, Surname, Gender, Date of birth, Place of Birth,
fiscal code (if not given by the user, is automatically calculated
calling the external function fiscal_code.py)  and finally
the vaccination date, chosen by the doctor  or suggested by the
software, are all stored in a new line of people_vaccoinated.csv.
"""

from csv import writer
from datetime import datetime, date
import pandas as pd
from checker import check_fiscalcode
from fiscal_code import fiscal_code_calculator
from booking import select_date


def add_element(nperson):
    """
    Add element is the function that
    asks for the personal information to
    the doctor and then add those information
    to the people_vaccinated.csv
    """

    if check_fiscalcode(nperson):
        print(
            "Sorry, but "
            + nperson
            + " fiscal code is already present "
            + "in the database, no reason to add again, thank you")

        result = "present"
    else:
        if len(nperson) != 16:
            print("Wrong fiscal code format")
        elif len(nperson) == 0:
            print("Let's continue!")

        numbers = "1234567890"
        right_name = False
        name = input("Please enter the name -> ")

        while not right_name:
            right_name = True

            if name == "":
                name = input("ERROR - Please enter the name -> ")
                right_name = False
            elif name[0] == " ":
                name = input("ERROR - Please enter the name -> ")
                right_name = False
            else:
                for letter in name:
                    if letter in numbers:
                        name = input("ERROR - Please enter the name -> ")
                        right_name = False

        name = name[0].upper() + name[1:]
        right_surname = False
        surname = input("Please enter the surname -> ")

        while not right_surname:
            right_surname = True

            if surname == "":
                surname = input("ERROR - Please enter the surname -> ")
                right_surname = False
            elif surname[0] == " ":
                surname = input("ERROR - Please enter the surname -> ")
                right_surname = False
            else:
                for letter in surname:
                    if letter in numbers:
                        surname = input("ERROR - Please enter the surname -> ")
                        right_surname = False

        surname = surname[0].upper() + surname[1:]
        gender = input("Please enter your gender: M or F -> ")

        while gender not in ["M", "m", "F", "f"]:
            gender = input(
                "ERROR - Please enter your gender: M or F -> "
            )

        gender = gender.upper()
        right_birthday = False
        birthday = input("Please enter the birthday gg/mm/yyyy -> ")

        while not right_birthday:
            right_birthday = True

            if not check_date_before(birthday):
                birthday = input("ERROR - Please enter the birthday gg/mm/yyyy -> ")
                right_birthday = False

        birthplace = input("Please enter the birth place -> ")
        belfiore = pd.read_csv("registry_codes.csv")

        while birthplace.lower() not in belfiore["Place"].tolist():
            birthplace = input(
                "ERROR - Please enter the birth place -> "
            )

        fiscalcode = fiscal_code_calculator(name, surname, birthday, gender, birthplace)

        if check_fiscalcode(fiscalcode):
            print("Sorry, but " + fiscalcode
                  + " fiscal code is already present in the database, thank you.")

        else:
            # ask to the patient if he/she is alre
            already_vaccinated = input(
                "Have you already received the first vaccine shot? Y or N: "
            )

            if already_vaccinated in ["Y", "y"]:
                # check if the date was inserted in the correct format
                check_format = False

                while not check_format:
                    # get the day of the first dose
                    firstdose = input(
                        "Enter the past date of the vaccination in the format gg/mm/yyyy "
                    )
                    if check_date_before(firstdose):
                        check_format = True
                    else:
                        print("ERROR")
            else:
                firstdose = select_date()

            # Open file in append mode
            with open("people_vaccinated.csv", "a", newline='') as peopledata:
                # Create a writer object from csv module
                csv_writer = writer(peopledata)
                # Add contents of list as last row in the csv file
                csv_writer.writerow(
                    [fiscalcode, name, surname, gender, birthday, birthplace, firstdose]
                )

            print("You succeffully registered", name, surname, "'s vaccination date!")
            result = True

    return result


def check_date_before(date_input):
    """
    The function checks if the input
    passed in the function is a valid date
    in the gg/mm/yyyy format and also checks that
    the date is before today.
    """

    if len(date_input) == 10:
        try:
            input_datetime = datetime.strptime(date_input, "%d/%m/%Y").date()
            today = date.today()
        except ValueError:
            result = False

        result = bool(input_datetime < today)
    else:
        result = False

    return result
