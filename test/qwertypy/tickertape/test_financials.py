import unittest
from unittest import TestCase

import src.qwertypy.tickertape.financials as ttFinancials

class TestMethods(TestCase):
    def test_getStatement(self):
        ttName = "reliance-industries-RELI"
        for statementType in ttFinancials.statementTypes:
            statement = ttFinancials.getStatement(ttName, statementType)
            self.assertEqual(type(statement), dict)

    def test_getYearsAndValues(self):
        ttName = "reliance-industries-RELI"
        statementType = ttFinancials.statementTypes["income"]
        statement = ttFinancials.getStatement(ttName, statementType)
        yearsAndValues = ttFinancials.getYearsAndValues(statement, "incDps")
        self.assertEqual(type(yearsAndValues), dict)
        self.assertEqual(type(yearsAndValues[list(yearsAndValues.keys())[0]]) in [int, float], True)

if __name__ == "main":
    unittest.main()