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


if __name__ == "__main__":
    unittest.main()
