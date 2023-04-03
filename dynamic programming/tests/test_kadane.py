import unittest
from ..kadane_algorithm import kadane as test_function


class UnitTestCase(unittest.TestCase):

    def test_basic_case1(self):
        nums = [2, 3, -1, 1]
        result = 5
        self.assertEqual(test_function(nums), result, "test_basic_case1")

    def test_basic_case2(self):
        nums = [5, 3, -3, 6, 9, -1, -3, 5, 6, -4]
        result = 27
        self.assertEqual(test_function(nums), result, "test_basic_case2")

    def test_empty(self):
        nums = []
        result = 0
        self.assertEqual(test_function(nums), result, "test_empty")

    def test_one_element_positive(self):
        nums = [3]
        result = 3
        self.assertEqual(test_function(nums), result, "test_one_element_positive")

    def test_one_element_negative(self):
        nums = [-5]
        result = -5
        self.assertEqual(test_function(nums), result, "test_one_element_negative")

    def test_two_element_negative(self):
        nums = [-5, -3]
        result = -3
        self.assertEqual(test_function(nums), result, "test_two_element_negative")


if __name__ == "__main__":
    unittest.main()
