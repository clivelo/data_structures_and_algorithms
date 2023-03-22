import unittest
from ..knapsack_recursion import knapsack_recursion as test_function


class UnitTestCase(unittest.TestCase):

    def test_basic_case(self):
        profits = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
        weights = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
        capacity = 165
        output = 309
        self.assertEqual(test_function(profits, weights, capacity), output, "test_basic_case")

    def test_zero_output(self):
        profits = [1, 2, 3]
        weights = [4, 5, 6]
        capacity = 3
        output = 0
        self.assertEqual(test_function(profits, weights, capacity), output, "test_zero_output")

    def test_pick_one(self):
        profits = [1, 2, 3]
        weights = [4, 5, 1]
        capacity = 4
        output = 3
        self.assertEqual(test_function(profits, weights, capacity), output, "test_pick_one")

    def test_not_complete_capacity(self):
        profits = [442, 525, 511, 593, 546, 564, 617]
        weights = [41, 50, 49, 59, 55, 57, 60]
        capacity = 170
        output = 1735
        self.assertEqual(test_function(profits, weights, capacity), output, "test_include_all")

    def test_include_all(self):
        profits = [1, 2, 3]
        weights = [4, 5, 6]
        capacity = 15
        output = 6
        self.assertEqual(test_function(profits, weights, capacity), output, "test_include_all")


if __name__ == "__main__":
    unittest.main()
