import unittest
import pandas as pd
from access_db import parse_args, save_new_username_correct, check_for_username_correct
from visualize import print_all_users, vaccinated_people, print_info
from adder import add_element
from checker import check_green_pass

class Test(unittest.TestCase):

    def setUp(self):

        self.T_fiscalcode = "MRTSAI99B52C957F"
        self.F_fiscalcode = "mrtsai99b52c957f"
        self.V_fiscalcode= ''
        self.database = "people_vaccinated.csv"
        self.A_username = 'Nicole00'
        self.A_password ='Lab2021'
        self.R_password= 'DataAnalyticsMaster'
        self.R_username= 'AndreaRocco'
        self.D_password= 'Wudy'
        self.D_username= 'RickyTrabu'
        self.W_username= 'ciao'
        self.W_password= 'hello'
        self.green_pass_fiscalcode = 'BNCMRC68E30A058X'
        self.wrong1_green_pass_fiscalcode = 'Alberto'
        self.wrong2_green_pass_fiscalcode = '10'
        self.wrong3_green_pass_fiscalcode = 'CCCMKI00E10L840D'







    def test_print_info(self):
        database = pd.DataFrame(pd.read_csv("../booking-pass/people_vaccinated.csv"))
        self.assertTrue(print_info(self.T_fiscalcode,database))
        self.assertFalse(print_info(self.F_fiscalcode,database))

    def test_check_for_username_correct(self):

        self.assertEqual('admin', check_for_username_correct(self.A_username,self.A_password))
        self.assertEqual('doctor', check_for_username_correct(self.D_username,self.D_password))
        self.assertEqual('restaurant', check_for_username_correct(self.R_username,self.R_password))
        self.assertEqual(0, check_for_username_correct(self.W_username,self.W_password))

    def test_add_element(self):
        self.assertTrue(add_element(self.F_fiscalcode))
        self.assertTrue(add_element(self.V_fiscalcode))
        self.assertEqual('present', add_element(self.T_fiscalcode))



    def test_check_green_pass(self):
        self.assertEqual('MRTSAI99B52C957F has the Green Pass.',check_green_pass(self.T_fiscalcode))
        self.assertEqual("BNCMRC68E30A058X doesn't have the Green Pass yet.", check_green_pass(self.green_pass_fiscalcode))
        self.assertEqual("Sorry, but 10 doesn't have the reservation for the vaccination.", check_green_pass(self.wrong2_green_pass_fiscalcode))
        self.assertEqual("Sorry, but CCCMKI00E10L840D doesn't have the reservation for the vaccination.", check_green_pass(self.wrong3_green_pass_fiscalcode))
        self.assertEqual("Sorry, but Alberto doesn't have the reservation for the vaccination.", check_green_pass(self.wrong1_green_pass_fiscalcode))










if __name__ == "__main__":
    unittest.main()
