"""
The module checker_greenpass.py focuses on checking
if the user is present in the csv file people_vaccinated.
In this way, it is possible to say if the user
has the GreenPass or not.
The user will have the GreenPass after 15 days from
the day of the vaccination (starting from the 15th day).
This information is accessible only to the restaurateur.
In order to do that, it is used the function CheckGreenPass().
"""

import csv
import pandas as pd
from checker import Check   
from datetime import date
# datetime moudule supplies classes for manipulating dates


nperson = input()
# nperson is the fiscal code of the user

def CheckGreenPass(nperson):
    """
    Since df['Date First Shot'] is a pandas.core.series.Series,
    the column's entries have to be transformed in datetime.
    In order to do that, the function pd.to_datetime is applied.
    """

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
        return "Sorry, but " + nperson + "doesn't even have the reservation for the vaccination."
    
