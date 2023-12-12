import unittest
from unittest import TestCase

import src.qwertypy.tickertape.financials as ttFinancials

class TestMethods(TestCase):
    def test_getStatement(self):
        ttName = "reliance-industries-RELI"
        for statementType in ttFinancials.statementTypes:
            statement = ttFinancials.getStatement(ttName, statementType)
            self.assertEqual(type(statement), dict)

if __name__ == "main":
    unittest.main()