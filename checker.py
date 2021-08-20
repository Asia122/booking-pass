"""
This module focuses on checking if the input
given by the user corresponds to one of the
instances present in the csv file.
"""
import pandas as pd


class Check:

    def check_fiscalcode(self, fiscalcode):
        """
        This function controls if the fiscal code given
        by the user is present in the fiscal code
        column inside the people_vaccinated csv file.
        """
        fiscalcode = fiscalcode.lower()
        db = pd.DataFrame(pd.read_csv('people_vaccinated.csv'))
        fcodes = db["Codice Fiscale"].str.lower()
        if fiscalcode in fcodes.values:
            return True
        return False
