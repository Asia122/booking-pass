import csv
import pandas as pd
from datetime import timedelta, date

nperson = input()
def CheckGreenPass(nperson):
    
    today = date.today()
    # return the current local date
    
    db = pd.DataFrame(pd.read_csv('people_vaccinated.csv'))
    db_datetime = pd.to_datetime(db["Date First Shot"])
    # pd.to_datetime converts argument to datetime
    
    if Check().check_fiscalcode(nperson):
        for row in db_datetime:
            end_date = row + timedelta(days=15)
            
            if end_date >= today:
                return nperson + "doesn't have the Green Pass yet."
            else:
                return nperson + " " + "has the Green Pass."
    
    else:
        return "Sorry, but " + nperson + " hasn't the green pass. "
    
