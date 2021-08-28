"""
The module checker_greenpass.py focuses on checking
if the user is present in the csv file people_vaccinated.
In this way, it is possible to say if the user
has the GreenPass or not.
The user will have the GreenPass after 15 days from
the day of the vaccination (included the 15th day).
This information is accessible only to the restaurateur.
In order to do that, it is used the function CheckGreenPass().
"""

import csv
import pandas as pd
from checker import Check   
from datetime import date, timedelta
# datetime moudule supplies classes for manipulating dates


nperson = input()
# nperson = fiscal code of the user

def CheckGreenPass(nperson):
    """
    Since df['Date First Shot'] is a pandas.core.series.Series,
    the column's entries have to be transformed in datetime.
    In order to do that, the function pd.to_datetime is applied.
    """

    today = date.today()
    # return the current local date
    
    if Check().check_fiscalcode(nperson):
        
        df = pd.DataFrame(pd.read_csv("people_vaccinated.csv"))
        
        nperson_date = df.loc[df["Fiscal Code"] == nperson,"Date First Shot"]        
        nperson_date = nperson_date.to_string()
        nperson_date = nperson_date[-10:]
        nperson_date = datetime.strptime(nperson_date,"%d/%m/%Y").date()
        
        end_date = nperson_date + timedelta(days=15)
        # green pass is valid after 15 days from the vaccination day
            
        if end_date > today:
            return nperson + " " + "doesn't have the Green Pass yet."
        else:
            return nperson + " " + "has the Green Pass."
    
    else:
        return "Sorry, but " + nperson + " " + "doesn't even have the reservation for the vaccination."
    
    
