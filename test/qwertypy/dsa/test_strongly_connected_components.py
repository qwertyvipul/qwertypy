import unittest
from unittest import TestCase
from collections import defaultdict

from src.qwertypy.dsa.strongly_connected_components import tarjanUndirected

def getGraph(edges):  
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph
        

class TestMethods(TestCase):
    def test_tarjanUndirected(self):
        edgesAndExpected = [
            [
                [[1,0],[0,2],[0,3],[0,4],[4,2],[2,3],[3,4]],
                {1: 0, 0: 1, 2: 1, 4: 1, 3: 1}
            ],
            [
                [[0,1],[2,0],[1,3],[3,4],[4,5],[5,6],[6,4]],
                {0: 0, 1: 1, 3: 2, 4: 3, 5: 3, 6: 3, 2: 6}
            ]
        ]

        for edges, expected in edgesAndExpected:
            graph = getGraph(edges)
            tu = tarjanUndirected(graph)
            for key in expected:
                self.assertEqual(tu[key], expected[key])

if __name__ == "main":
    unittest.main()