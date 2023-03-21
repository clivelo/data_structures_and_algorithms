import unittest
from ..bubble_sort import bubble_sort as test_function


class UnitTestCase(unittest.TestCase):

    def test_basic_sort(self):
        l1 = [4, 7, 3, 5, 6, 2, 1]
        l2 = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(test_function(l1), l2, "test_basic_sort")

    def test_negative_number_sort(self):
        l1 = [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
        l2 = [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]
        self.assertEqual(test_function(l1), l2, "test_negative_number_sort")

    def test_already_sorted(self):
        l1 = [-5, -1, 3, 5, 8, 9, 20, 99]
        l2 = [-5, -1, 3, 5, 8, 9, 20, 99]
        self.assertEqual(test_function(l1), l2, "test_already_sorted")

    def test_repeated_elements(self):
        l1 = [5, -12, 6, 5, 99, -7, 9, -12, 5, 21, 9, 9, 1, -7]
        l2 = [-12, -12, -7, -7, 1, 5, 5, 5, 6, 9, 9, 9, 21, 99]
        self.assertEqual(test_function(l1), l2, "test_repeated_elements")

    def test_empty_list(self):
        l1 = []
        l2 = []
        self.assertEqual(test_function(l1), l2, "test_empty_list")

    def test_one_element(self):
        l1 = [23]
        l2 = [23]
        self.assertEqual(test_function(l1), l2, "test_one_element")

    def test_one_element_repeated(self):
        l1 = [42, 42, 42, 42, 42, 42, 42]
        l2 = [42, 42, 42, 42, 42, 42, 42]
        self.assertEqual(test_function(l1), l2, "test_one_element_repeated")

    def test_long_list(self):
        import random

        l1 = list(range(10000))
        l2 = list(range(10000))
        random.shuffle(l1)
        self.assertEqual(test_function(l1), l2, "test_long_list")


if __name__ == "__main__":
    unittest.main()
