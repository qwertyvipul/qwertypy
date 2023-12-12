import unittest
from unittest import TestCase

import src.qwertypy.data_analysis.regression as qpyRegression
import src.qwertypy.data_plots.trend_plot as qpyTrendPlot
import src.qwertypy.tickertape.financials as ttFinancials


class TestMethods(TestCase):
    @unittest.skip("Use when required")
    def test_trendPlot(self):
        ttName = "reliance-industries-RELI"
        statementType = ttFinancials.statementTypes["income"]
        statement = ttFinancials.getStatement(ttName, statementType)
        yearsAndValues = ttFinancials.getYearsAndValues(statement, "incTrev")
        xTrain = [int(x) for x in list(yearsAndValues.keys())]
        yTrain = [yearsAndValues[x] for x in yearsAndValues]
        model = qpyRegression.QpyLinearRegression(xTrain, yTrain)
        model.train()
        yPredict = [round(val, 2) for val in model.getPrediction()]
        qpyTrendPlot.trendPlot(
            xTrain, yTrain, 
            "xLabel", "yLabel", "plotTitle",
            trendValues = yPredict,
            legends = ["barLegend", "trendLegend"],
            text = "text", watermark = "watermark",
            saveToFile = "testImage.jpg"
        )

if __name__ == "main":
    unittest.main()