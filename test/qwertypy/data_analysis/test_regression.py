import unittest
from unittest import TestCase

import src.qwertypy.data_analysis.regression as qpyRegression

class TestMethods(TestCase):
    def test_regressionModel(self):
        xTrain = [1, 2, 3, 4, 5, 6]
        yTrain = [2, 4, 6, 8, 10, 12]
        model = qpyRegression.QpyLinearRegression(xTrain, yTrain)
        model.train()
        yPredict = model.getPrediction()
        for y1, y2 in zip(yPredict, yTrain):
            self.assertAlmostEqual(y1, y2, 0, 
                "Prediction {} is not almost equal to training {}!".format(y1, y2)
            )

        xPredict2 = [10, 11]
        yExpected = [20, 22]
        yPredict2 = model.getPrediction(xPredict2)
        for y1, y2 in zip(yPredict2, yExpected):
            self.assertAlmostEqual(y1, y2, 0, 
                "Prediction {} is not almost equal to training {}!".format(y1, y2)
            )
        

if __name__ == "main":
    unittest.main()