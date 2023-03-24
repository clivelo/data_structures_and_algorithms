import unittest
from ..graph import Graph


class UnitTestCase(unittest.TestCase):

    def test_basic_case(self):
        graph = Graph(6, [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (3, 5, 11), (4, 3, 4)],
                      weighted=True, directed=True)
        node = graph.dijkstra(0, 5)
        output = 20
        self.assertEqual(node, output, "test_basic_case")

    def test_large_graph1(self):
        graph = Graph(9, [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2),
                          (2, 3, 6), (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)],
                      weighted=True)
        node = graph.dijkstra(0, 7)
        output = 7
        self.assertEqual(node, output, "test_large_graph1")

    def test_large_graph2(self):
        graph = Graph(9, [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2),
                          (2, 3, 6), (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)],
                      weighted=True)
        node = graph.dijkstra(0, 4)
        output = 3
        self.assertEqual(node, output, "test_large_graph2")

    def test_large_graph3(self):
        graph = Graph(9, [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2),
                          (2, 3, 6), (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)],
                      weighted=True)
        node = graph.dijkstra(2, 8)
        output = 12
        self.assertEqual(node, output, "test_large_graph3")


if __name__ == "__main__":
    unittest.main()
