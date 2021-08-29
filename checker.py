"""
The module checker_greenpass.py focuses on checking
if a oerson has the GreenPass or not.
In order to establish it, the date of the vaccination
must be checked. If 15 days have passed from that date,
(including the 15th day) the user has the GreenPass, otherwise not.
This information is accessible only to the restaurateur.
In order to do that, the function CheckGreenPass() is used.
"""

"""
First of all, it has to be checked if the user
is present in the csv file people_vaccinated.
If not, it means it doesn't even have the reservation
for the vaccination.
"""
import csv
import datetime
import pandas as pd 
from datetime import date, timedelta, datetime
import pandas as pd


class Check:

    def check_fiscalcode(self, nperson):
        """
        This function controls if the fiscal code given
        by the user is present in the fiscal code
        column inside the people_vaccinated csv file.
        """
        fiscalcode = nperson.lower()
        db = pd.DataFrame(pd.read_csv('people_vaccinated.csv'))
        fcodes = db["Fiscal Code"].str.lower()
        if fiscalcode in fcodes.values:
            return True
        return False


    # nperson = fiscal code of the user

    def CheckGreenPass(self, nperson):
    
        today = date.today()
        # return the current local date (without the time)
    
        if Check().check_fiscalcode(nperson):
        
            df = pd.DataFrame(pd.read_csv("people_vaccinated.csv"))
            
            nperson_date = df.loc[df["Fiscal Code"] == nperson,"Date First Shot"]
            # to select the corresponding date of vaccination given the fiscal code of the user
            
            nperson_date = nperson_date.to_string()
            nperson_date = nperson_date[-10:]
            nperson_date = datetime.strptime(nperson_date,"%d/%m/%Y").date()
            
            """
            Since the column df["Date First Shot"] is a pandas.core.series.Series,
            the column's entries have to be transformed in datetime.
            """
            
            end_date = nperson_date + timedelta(days=15)
            # green pass is valid after 15 days from the vaccination day
            
            """
            if nperson_date + 15 days = today --> YES GreenPass
            if nperson_date + 15 days < today --> YES GreenPass
            if nperson_date + 15 days > today --> NO GreenPass
            """
                
            if end_date > today:
                print(nperson + " " + "doesn't have the Green Pass yet.")
            else:
                print( nperson + " " + "has the Green Pass.")
    
        else:
            print("Sorry, but " + nperson + " " + "doesn't even have the reservation for the vaccination.")
   


