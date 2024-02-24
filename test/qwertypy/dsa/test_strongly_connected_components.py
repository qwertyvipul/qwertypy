import unittest
from unittest import TestCase
from collections import defaultdict

from src.qwertypy.dsa.strongly_connected_components import tarjan

class TestMethods(TestCase):
    def test_fw(self):
        edges = [[0,1],[2,0],[1,3],[3,4],[4,5],[5,6],[6,4]]  
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        self.assertEqual(tarjan(graph), {0: 0, 1: 1, 3: 3, 4: 4, 5: 4, 6: 4, 2: 2})

if __name__ == "main":
    unittest.main()