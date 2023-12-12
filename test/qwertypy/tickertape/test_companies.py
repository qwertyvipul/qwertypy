import unittest
from unittest import TestCase

import src.qwertypy.tickertape.companies as ttCompanies

class TestMethods(TestCase):
    def test_getTopCompanies(self):
        topCompanies = ttCompanies.getTopCompanies()
        self.assertEqual(type(topCompanies), list, "getTopCompanies should return a list")
        self.assertEqual(type(topCompanies[0]), str, "getTopCompanies should return a list of strings")
        self.assertEqual(len(topCompanies), 100, "Number of top companies should be 100")

    @unittest.skip("Skipping unittest to save time")
    def test_getAllCompanies(self):
        allCompanies = ttCompanies.getAllCompanies()
        self.assertEqual(type(allCompanies), list, "getAllCompanies should return a list")
        self.assertEqual(type(allCompanies[0]), str, "getAllCompanies should return a list of strings")

    def test_getCompanyInfo(self):
        ttName = "reliance-industries-RELI"
        companyInfo = ttCompanies.getCompanyInfo(ttName)
        self.assertEqual(companyInfo, dict(ttName=ttName, name="Reliance Industries Ltd", ticker="RELIANCE"))

if __name__ == "main":
    unittest.main()