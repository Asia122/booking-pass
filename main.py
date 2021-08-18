
"WRITE THE PROGRAM DESCRIPTION"
#LAVORIAMO QUI


import argparse
import pandas as pd

db = pd.DataFrame(pd.read_csv('people_vaccinated.csv'))

parser = argparse.ArgumentParser(description='This program will' +
                                             ' check if the given personal information are correct' +
                                             ' write in a dataset the date of your vaccination ' +
                                             ' check if in a given date you will have the green pass ')
#la descrizione va fatta meglio
group = parser.add_mutually_exclusive_group()
parser.add_argument("name", help="input the fiscal code o a person")

# -d per far uscire tutto il dataset
group.add_argument("-d", "--database", action="store_true",
                   help="add a new")
args = parser.parse_args()
answer = args.name

if args.database:
    print("Now you can see by yourself if " +
          answer + " fiscal code is present in our database manually")
    print(db)
    
print(db["Codice Fiscale"].loc[db["Codice Fiscale"].str.lower() == answer.lower()]
              .values[0], "is the fiscal code of",
              db["Nome"].loc[db["Codice Fiscale"].str.lower() ==
              answer.lower()].values[0],
              db["Cognome"].loc[db["Codice Fiscale"].str.lower() ==
              answer.lower()].values[0], "whose first dose date is on",
              db["Data prima dose"].loc[db["Codice Fiscale"].str.lower() ==
              answer.lower()].values[0])



