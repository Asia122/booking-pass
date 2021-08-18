
"WRITE THE PROGRAM DESCRIPTION"


import argparse
import pandas as pd

db = pd.DataFrame(pd.read_csv('people_vaccinated.csv'))

parser = argparse.ArgumentParser(description='This program will' +
                                             ' check if the given personal information are correct' +
                                             ' write in a dataset the date of your vaccination ' +
                                             ' check if in a given date you will have the green pass ')
#la descrizione va fatta meglio

parser.add_argument("name", help="input the name of a known guitarist or band")
args = parser.parse_args()
answer = args.name

print(db["Codice Fiscale"].loc[db["Codice Fiscale"].str.lower() == answer.lower()]
              .values[0], "is the fiscal code of",
              db["Nome"].loc[db["Codice Fiscale"].str.lower() ==
              answer.lower()].values[0],
              db["Cognome"].loc[db["Codice Fiscale"].str.lower() ==
              answer.lower()].values[0], "whose first dose date is on",
              db["Data prima dose"].loc[db["Codice Fiscale"].str.lower() ==
              answer.lower()].values[0])

