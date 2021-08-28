
"WRITE THE PROGRAM DESCRIPTION"
#LAVORIAMO QUI


import argparse
import pandas as pd
from adder import add_element
from checker import Check

db = pd.DataFrame(pd.read_csv('people_vaccinated.csv'))

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

group.add_argument("-a", "--add", action="store_true",
                   help="add a new vaccinated or to be vaccinated person to the database")

args = parser.parse_args()
answer = args.name

if args.database:
    print("Now you can see by yourself if " +
          answer + " fiscal code is present in our database manually")
    print(db)
if args.add:
        add_element(answer)
else:
    print(db["Fiscal Code"].loc[db["Fiscal Code"].str.lower() == answer.lower()].values[0], "is the fiscal code of",
    db["Name"].loc[db["Fiscal Code"].str.lower() == answer.lower()].values[0],
    db["Surname"].loc[db["Fiscal Code"].str.lower() ==
    answer.lower()].values[0], "whose first dose date is on",
    db["Date First Shot"].loc[db["Fiscal Code"].str.lower() ==
    answer.lower()].values[0])



