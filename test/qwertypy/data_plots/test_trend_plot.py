
import random
import unittest

from unittest import TestCase

import src.qwertypy.data_plots.trend_plot as qpyTrendPlot

class TestMethods(TestCase):
    # @unittest.skip("Use when required")
    def test_trendPlot(self):
        xValues = [i for i in range(10)]
        yValues = [random.randint(1, 10) for _ in range(10)]
        xTicks = ["xTick" + str(i+1) for i in range(10)]
        trendValues = list(yValues)
        qpyTrendPlot.trendPlot(
            xValues, yValues,
            # xTicks = xValues, 
            rotateXTicks = 90,
            xLabel = "xLabel", 
            yLabel = "yLabel", 
            plotTitle = "plotTitle",
            trendValues = trendValues,
            legends = ["trendLegend", "barLegend"],
            text = "text", 
            textBackground = "red",
            watermark = "watermark",
            showValues = True,
            # saveToFile = "testImage.jpg"
        )

if __name__ == "main":
    unittest.main()