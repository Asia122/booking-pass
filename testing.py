"""
This module is the one that tests some of the functions
necessary to let the user interact with the database.
Each Test Case tests a valid and invalid entries.
SetUp functions were used as well
to set up mock variables.
"""

import unittest
import pandas as pd
from access_db import check_for_username_correct
from visualize import print_info
from adder import add_element
from checker import check_green_pass


class Test(unittest.TestCase):
    """
    Class that automatically tests the various
    cases on the fundamental functions that are
    used in the main.py
    """

    def setUp(self):
        """
        The setup() function runs when the program starts.
        It is used to set the initial environment properties
        """

        self.t_fiscalcode = "MRTSAI99B52C957F"
        self.f_fiscalcode = "mrtsai99b52c957f"
        self.v_fiscalcode = ''
        self.database = "people_vaccinated.csv"
        self.a_username = 'Nicole00'
        self.a_password = 'Lab2021'
        self.r_password = 'DataAnalyticsMaster'
        self.r_username = 'AndreaRocco'
        self.d_password = 'Wudy'
        self.d_username = 'RickyTrabu'
        self.w_username = 'ciao'
        self.w_password = 'hello'
        self.green_pass_fiscalcode = 'BNCMRC68E30A058X'
        self.wrong1_green_pass_fiscalcode = 'Alberto'
        self.wrong2_green_pass_fiscalcode = '10'
        self.wrong3_green_pass_fiscalcode = 'CCCMKI00E10L840D'

    def test_print_info(self):
        """
        This function is in the module visualize.py
        """

        database = pd.DataFrame(pd.read_csv("../booking-pass/people_vaccinated.csv"))
        self.assertTrue(print_info(self.t_fiscalcode, database))
        self.assertFalse(print_info(self.f_fiscalcode, database))

    def test_check_for_username_correct(self):
        """
        This function is in the module access_db.py
        """

        self.assertEqual('admin',
                         check_for_username_correct(self.a_username, self.a_password))
        self.assertEqual('doctor',
                         check_for_username_correct(self.d_username, self.d_password))
        self.assertEqual('restaurant',
                         check_for_username_correct(self.r_username, self.r_password))
        self.assertEqual(0, check_for_username_correct(self.w_username, self.w_password))

    def test_add_element(self):
        """
        This function is in the module adder.py
        """

        self.assertTrue(add_element(self.f_fiscalcode))
        self.assertEqual('present', add_element(self.t_fiscalcode))

    def test_2_add_elemet(self):
        """
        This function is in the module adder.py
        """

        self.assertTrue(add_element(self.v_fiscalcode))

    def test_check_green_pass(self):
        """
        This function is in the module checker.py
        """

        self.assertEqual('MRTSAI99B52C957F has the Green Pass.',
                         check_green_pass(self.t_fiscalcode))
        self.assertEqual("BNCMRC68E30A058X doesn't have the Green Pass yet.",
                         check_green_pass(self.green_pass_fiscalcode))
        self.assertEqual("Wrong fiscal code format",
                         check_green_pass(self.wrong2_green_pass_fiscalcode))
        self.assertEqual("Sorry, but CCCMKI00E10L840D doesn't have the reservation " +
                         "for the vaccination.",
                         check_green_pass(self.wrong3_green_pass_fiscalcode))
        self.assertEqual("Wrong fiscal code format",
                         check_green_pass(self.wrong1_green_pass_fiscalcode))

# by setting this up we can run this file
# on the command line without having
# having to call the unittest module.


if __name__ == "__main__":
    unittest.main()
