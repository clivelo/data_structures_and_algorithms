import unittest
from ..tree_node import TreeNode
from ..helper import parse_list as test_function, equals


class UnitTestCase(unittest.TestCase):

    def test_none_equal(self):
        t1 = test_function([None])
        t2 = None
        self.assertTrue(equals(t1, t2), "test_none_equal")

    def test_none_not_equal(self):
        t1 = test_function([3])
        t2 = None
        self.assertFalse(equals(t1, t2), "test_none_not_equal")

    def test_one_node_equal(self):
        t1 = test_function([5])
        t2 = TreeNode(5)
        self.assertTrue(equals(t1, t2), "test_one_node_equal")

    def test_one_node_not_equal(self):
        t1 = test_function([8])
        t2 = TreeNode(5)
        self.assertFalse(equals(t1, t2), "test_one_node_not_equal")

    def test_two_nodes_equal(self):
        t1 = test_function([5, 3])
        t2 = TreeNode(5)
        t2.left = TreeNode(3)
        self.assertTrue(equals(t1, t2), "test_two_nodes_equal")

    def test_two_nodes_not_equal(self):
        t1 = test_function([5, 3])
        t2 = TreeNode(5)
        t2.left = TreeNode(4)
        self.assertFalse(equals(t1, t2), "test_two_nodes_not_equal")

    def test_three_nodes_equal(self):
        t1 = test_function([5, 3, 8])
        t2 = TreeNode(5)
        t2.left = TreeNode(3)
        t2.right = TreeNode(8)
        self.assertTrue(equals(t1, t2), "test_three_nodes_equal")

    def test_three_nodes_not_equal(self):
        t1 = test_function([5, 4, 7])
        t2 = TreeNode(5)
        t2.left = TreeNode(4)
        t2.right = TreeNode(8)
        self.assertFalse(equals(t1, t2), "test_three_nodes_not_equal")

    def test_two_nodes_split(self):
        t1 = TreeNode(5)
        t1.left = TreeNode(3)
        t2 = test_function([5, None, 3])
        self.assertFalse(equals(t1, t2), "test_two_nodes_split")

    def test_three_nodes_swap(self):
        t1 = test_function([5, 3, 7])
        t2 = TreeNode(5)
        t2.left = TreeNode(7)
        t2.right = TreeNode(3)
        self.assertFalse(equals(t1, t2), "test_three_nodes_swap")

    def test_left_skewed_tree_equal(self):
        t1 = test_function([10, 8, 11, 6, None, None, None, 4, None, 3, 5])
        t2 = TreeNode(10)
        t2.left = TreeNode(8)
        t2.right = TreeNode(11)
        t2.left.left = TreeNode(6)
        t2.left.left.left = TreeNode(4)
        t2.left.left.left.left = TreeNode(3)
        t2.left.left.left.right = TreeNode(5)
        self.assertTrue(equals(t1, t2), "test_left_skewed_tree_equal")

    def test_left_skewed_tree_not_equal(self):
        t1 = test_function([10, 8, 11, 6, None, None, None, 4, None, 3])
        t2 = TreeNode(10)
        t2.left = TreeNode(8)
        t2.right = TreeNode(11)
        t2.left.left = TreeNode(6)
        t2.left.left.left = TreeNode(4)
        t2.left.left.left.left = TreeNode(3)
        t2.left.left.left.right = TreeNode(5)
        self.assertFalse(equals(t1, t2), "test_left_skewed_tree_not_equal")

    def test_balanced_tree_equal(self):
        t1 = test_function([10, 8, 12, 7, 9, None, 13])
        t2 = TreeNode(10)
        t2.left = TreeNode(8)
        t2.right = TreeNode(12)
        t2.left.left = TreeNode(7)
        t2.left.right = TreeNode(9)
        t2.right.right = TreeNode(13)
        self.assertTrue(equals(t1, t2), "test_balanced_tree_equal")

    def test_balanced_tree_not_equal(self):
        t1 = test_function([10, 8, 12, 7, 9, 11])
        t2 = TreeNode(10)
        t2.left = TreeNode(8)
        t2.right = TreeNode(12)
        t2.left.left = TreeNode(7)
        t2.left.right = TreeNode(9)
        t2.right.right = TreeNode(13)
        self.assertFalse(equals(t1, t2), "test_balanced_tree_not_equal")


if __name__ == "__main__":
    unittest.main()
