""" System Module """
from datetime import date, timedelta, datetime
import pandas as pd

"""
The module checker.py focuses on checking
if a person has the GreenPass or not.
In order to establish it, the date of the vaccination
must be checked. If 15 days have passed from that date,
(including the 15th day) the user has the GreenPass, otherwise not.
This information is accessible only to the restaurateur.
In order to do that, the function check_green_pass() is used.

First of all, it has to be checked if the user
is present in the csv file people_vaccinated.
If not, it means it doesn't even have the reservation
for the vaccination.
"""


def check_fiscalcode(nperson):
    # nperson = fiscal code of the user

    """
    This function controls if the fiscal code given
    by the user is present in the fiscal code
    column inside the people_vaccinated csv file.
    """

    fiscalcode = nperson.lower()
    vaccinated_df = pd.DataFrame(pd.read_csv('people_vaccinated.csv'))
    fcodes = vaccinated_df["Fiscal Code"].str.lower()
    if fiscalcode in fcodes.values:
        return True
    return False


def check_green_pass(nperson):

    today = date.today()
    # return the current local date (without the time)

    if check_fiscalcode(nperson):

        vaccinated_df = pd.DataFrame(pd.read_csv("people_vaccinated.csv"))

        pers_date = vaccinated_df.loc[vaccinated_df["Fiscal Code"] == nperson,
                                      "Date First Shot"]
        # to select the corresponding date of vaccination given
        # the fiscal code of the user

        pers_date = pers_date.to_string()
        pers_date = pers_date[-10:]
        pers_date = datetime.strptime(pers_date, "%d/%m/%Y").date()

        # Since the column df["Date First Shot"] is
        # a pandas.core.series.Series,
        # the column's entries have to be transformed in datetime.

        end_date = pers_date + timedelta(days=15)
        # green pass is valid after 15 days from the vaccination day

        # if nperson_date + 15 days = today --> YES GreenPass
        # if nperson_date + 15 days < today --> YES GreenPass
        # if nperson_date + 15 days > today --> NO GreenPass

        if end_date > today:
            return nperson + " " + "doesn't have the Green Pass yet."
        else:
            return nperson + " " + "has the Green Pass."

    else:
        result = "Sorry, but " + nperson + " "
        result = result + "doesn't have the reservation for the vaccination."

        return result
