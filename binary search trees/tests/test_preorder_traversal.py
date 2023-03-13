import unittest
from ..helper import parse_list
from ..preorder_traversal import preorder_traverse as test_function


class UnitTestCase(unittest.TestCase):

    def test_no_node_equal(self):
        t1 = test_function(None)
        t2 = []
        self.assertEqual(t1, t2, "test_no_node_equal")

    def test_no_node_not_equal(self):
        t1 = test_function(None)
        t2 = [2]
        self.assertNotEqual(t1, t2, "test_no_node_not_equal")

    def test_one_node_equal(self):
        t1 = test_function(parse_list([5]))
        t2 = [5]
        self.assertEqual(t1, t2, "test_one_node_equal")

    def test_one_node_not_equal(self):
        t1 = test_function(parse_list([5]))
        t2 = [4]
        self.assertNotEqual(t1, t2, "test_one_node_not_equal")

    def test_two_node_equal(self):
        t1 = test_function(parse_list([5, 3]))
        t2 = [5, 3]
        self.assertEqual(t1, t2, "test_two_node_equal")

    def test_two_node_not_equal(self):
        t1 = test_function(parse_list([5, 3]))
        t2 = [3, 5]
        self.assertNotEqual(t1, t2, "test_two_node_not_equal")

    def test_three_node_equal(self):
        t1 = test_function(parse_list([5, 3, 7]))
        t2 = [5, 3, 7]
        self.assertEqual(t1, t2, "test_three_node_equal")

    def test_three_node_not_equal(self):
        t1 = test_function(parse_list([5, 3, 7]))
        t2 = [3, 5, 7]
        self.assertNotEqual(t1, t2, "test_three_node_not_equal")

    def test_imbalance_tree_equal(self):
        t1 = test_function(parse_list([7, 5, None, 3, 6]))
        t2 = [7, 5, 3, 6]
        self.assertEqual(t1, t2, "test_imbalance_tree_equal")

    def test_imbalance_tree_not_equal(self):
        t1 = test_function(parse_list([7, 5, None, 3, 6]))
        t2 = [3, 5, 6, 7]
        self.assertNotEqual(t1, t2, "test_imbalance_tree_not_equal")

    def test_large_tree_equal(self):
        t1 = test_function(parse_list([2, 3, 5, 1, None, 3, 7, None, None, None, 4, 6, 8]))
        t2 = [2, 3, 1, 5, 3, 4, 7, 6, 8]
        self.assertEqual(t1, t2, "test_large_tree_equal")


if __name__ == "__main__":
    unittest.main()
