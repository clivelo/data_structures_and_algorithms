import unittest
from ..graph import Graph


class UnitTestCase(unittest.TestCase):

    def test_basic_case(self):
        graph = Graph(5, [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)])
        dfs = graph.dfs(3)
        output = [3, 4, 1, 2, 0]
        self.assertEqual(dfs, output, "test_basic_case")

    def test_weighted_graph(self):
        graph = Graph(9, [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2),
                          (2, 3, 6), (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)],
                      weighted=True)
        dfs = graph.dfs(0)
        output = [0, 8, 4, 3, 2, 5, 6, 7, 1]
        self.assertEqual(dfs, output, "test_weighted_graph")


if __name__ == "__main__":
    unittest.main()
