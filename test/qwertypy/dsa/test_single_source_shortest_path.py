import unittest
from unittest import TestCase
from collections import defaultdict

from src.qwertypy.dsa.single_source_shortest_path import dijkstra

class TestMethods(TestCase):
    def test_fw(self):
        n = 9
        edges = [
            (0, 1, 4),
            (0, 7, 8),
            (1, 7, 11),
            (1, 2, 8),
            (7, 8, 7),
            (7, 6, 1),
            (2, 8, 2),
            (8, 6, 6),
            (2, 3, 7),
            (2, 5, 4),
            (6, 5, 2),
            (3, 5, 14),
            (3, 4, 9),
            (5, 4, 10)
        ]

        graph = defaultdict(lambda: defaultdict(int))
        for u, v, d in edges:
            graph[u][v] = graph[v][u] = d

        self.assertEqual(dijkstra(graph, 0, n), [0, 4, 12, 19, 21, 11, 9, 8, 14])
        self.assertEqual(dijkstra(graph, 1, n), [4, 0, 8, 15, 22, 12, 12, 11, 10])

if __name__ == "main":
    unittest.main()