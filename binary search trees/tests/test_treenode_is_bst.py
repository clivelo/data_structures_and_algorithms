import unittest
from ..helper import parse_list, print_tree


class UnitTestCase(unittest.TestCase):

    def test_one_node_true(self):
        tree = parse_list([5])
        self.assertTrue(tree.is_bst(), "test_one_node_true")

    def test_two_node_true(self):
        tree = parse_list([5, 3])
        self.assertTrue(tree.is_bst(), "test_two_node_true")

    def test_two_node_false(self):
        tree = parse_list([3, 5])
        self.assertFalse(tree.is_bst(), "test_two_node_false")

    def test_three_node_true(self):
        tree = parse_list([5, 3, 7])
        self.assertTrue(tree.is_bst(), "test_three_node_true")

    def test_three_node_false(self):
        tree = parse_list([5, 3, 4])
        self.assertFalse(tree.is_bst(), "test_three_node_false")

    def test_imbalance_tree_true(self):
        tree = parse_list([7, 5, None, 3, 6])
        self.assertTrue(tree.is_bst(), "test_imbalance_tree_true")

    def test_imbalance_tree_false(self):
        tree = parse_list([7, 5, None, 6, 3])
        self.assertFalse(tree.is_bst(), "test_imbalance_tree_false")

    def test_large_tree_true(self):
        tree = parse_list([25, 15, 50, 10, 22, 35, 70, 4, None, 18, 24, None, 44, 66, 90])
        self.assertTrue(tree.is_bst(), "test_large_tree_true")

    def test_imbalanced_large_tree_true(self):
        tree = parse_list([3, 2, 7, 1, None, 4, 9, None, None, None, 5, 8, 10])
        self.assertTrue(tree.is_bst(), "test_imbalanced_large_tree_true")

    def test_imbalanced_large_tree_false(self):
        tree = parse_list([3, 2, 7, 1, None, 4, 9, None, None, None, 3, 8, 10])
        self.assertFalse(tree.is_bst(), "test_imbalanced_large_tree_true")


if __name__ == "__main__":
    unittest.main()
