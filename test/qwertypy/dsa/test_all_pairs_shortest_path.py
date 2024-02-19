import unittest
from unittest import TestCase
from collections import defaultdict

from src.qwertypy.dsa.all_pairs_shortest_path import fw

class TestMethods(TestCase):
    def test_fw(self):
        edges = [
            [1, 2, 3],
            [1, 4, 7],
            [2, 1, 8],
            [2, 3, 2],
            [3, 1, 5],
            [3, 4, 1],
            [4, 1, 2]
        ]
        graph = defaultdict(dict)
        for u, v, cost in edges:
            graph[u-1][v-1] = cost
        self.assertEqual(fw(graph, len(graph)), [[0, 3, 5, 6], [5, 0, 2, 3], [3, 6, 0, 1], [2, 5, 7, 0]])

if __name__ == "main":
    unittest.main()