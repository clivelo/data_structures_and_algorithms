import unittest
from ..lcs_memoization import lcs_memoization as test_function


class UnitTestCase(unittest.TestCase):

    def test_basic_case1(self):
        length = test_function("serendipitous", "precipitation")
        output = 7
        self.assertEqual(length, output, "test_basic_case1")

    def test_basic_case2(self):
        length = test_function("function", "tonnes")
        output = 3
        self.assertEqual(length, output, "test_basic_case2")

    def test_no_common(self):
        length = test_function("abcdef", "qrstuv")
        output = 0
        self.assertEqual(length, output, "test_no_common")

    def test_complete_subsequence(self):
        length = test_function("cat", "scatterplot")
        output = 3
        self.assertEqual(length, output, "test_complete_subsequence")

    def test_one_sequence_empty(self):
        length = test_function("harmonious", "")
        output = 0
        self.assertEqual(length, output, "test_one_sequence_empty")

    def test_both_sequences_empty(self):
        length = test_function("", "")
        output = 0
        self.assertEqual(length, output, "test_both_sequences_empty")


if __name__ == "__main__":
    unittest.main()
