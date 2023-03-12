import unittest
from ..tree_node import TreeNode
from ..helper import equals as test_function


class UnitTestCase(unittest.TestCase):

    def test_none_equal(self):
        t1 = None
        t2 = None
        self.assertTrue(test_function(t1, t2), "test_none_equal")

    def test_none_not_equal(self):
        t1 = None
        t2 = TreeNode(3)
        self.assertFalse(test_function(t1, t2), "test_none_not_equal")

    def test_one_node_equal(self):
        t1 = TreeNode(5)
        t2 = TreeNode(5)
        self.assertTrue(test_function(t1, t2), "test_one_node_equal")

    def test_one_node_not_equal(self):
        t1 = TreeNode(8)
        t2 = TreeNode(5)
        self.assertFalse(test_function(t1, t2), "test_one_node_not_equal")

    def test_two_nodes_equal(self):
        t1 = TreeNode(5)
        t1.left = TreeNode(3)
        t2 = TreeNode(5)
        t2.left = TreeNode(3)
        self.assertTrue(test_function(t1, t2), "test_two_nodes_equal")

    def test_two_nodes_not_equal(self):
        t1 = TreeNode(5)
        t1.left = TreeNode(3)
        t2 = TreeNode(5)
        t2.left = TreeNode(4)
        self.assertFalse(test_function(t1, t2), "test_two_nodes_not_equal")

    def test_three_nodes_equal(self):
        t1 = TreeNode(5)
        t1.left = TreeNode(3)
        t1.right = TreeNode(8)
        t2 = TreeNode(5)
        t2.left = TreeNode(3)
        t2.right = TreeNode(8)
        self.assertTrue(test_function(t1, t2), "test_three_nodes_equal")

    def test_three_nodes_not_equal(self):
        t1 = TreeNode(5)
        t1.left = TreeNode(4)
        t1.right = TreeNode(7)
        t2 = TreeNode(5)
        t2.left = TreeNode(4)
        t2.right = TreeNode(8)
        self.assertFalse(test_function(t1, t2), "test_three_nodes_not_equal")

    def test_two_nodes_split(self):
        t1 = TreeNode(5)
        t1.left = TreeNode(3)
        t2 = TreeNode(5)
        t2.right = TreeNode(3)
        self.assertFalse(test_function(t1, t2), "test_two_nodes_split")

    def test_three_nodes_swap(self):
        t1 = TreeNode(5)
        t1.left = TreeNode(3)
        t1.right = TreeNode(7)
        t2 = TreeNode(5)
        t2.left = TreeNode(7)
        t2.right = TreeNode(3)
        self.assertFalse(test_function(t1, t2), "test_three_nodes_swap")


if __name__ == "__main__":
    unittest.main()
