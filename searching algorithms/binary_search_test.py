import unittest
from binary_search import binary_search as test_function


class UnitTestCase(unittest.TestCase):

    def test_middle(self):
        cards = [13, 11, 10, 7, 4, 3, 1, 0]
        query = 7
        output = 3
        result = test_function(cards, query)
        self.assertEqual(result, output)

    def test_near_end(self):
        cards = [13, 11, 10, 7, 4, 3, 1, 0]
        query = 1
        output = 6
        result = test_function(cards, query)
        self.assertEqual(result, output)

    def test_beginning(self):
        cards = [4, 2, 1, -1]
        query = 4
        output = 0
        result = test_function(cards, query)
        self.assertEqual(result, output)

    def test_end(self):
        cards = [3, -1, -9, -127]
        query = -127
        output = 3
        result = test_function(cards, query)
        self.assertEqual(result, output)

    def test_single_element(self):
        cards = [6]
        query = 6
        output = 0
        result = test_function(cards, query)
        self.assertEqual(result, output)

    def test_not_found(self):
        cards = [9, 7, 5, 2, -9]
        query = 4
        output = -1
        result = test_function(cards, query)
        self.assertEqual(result, output)

    def test_empty_list(self):
        cards = []
        query = 7
        output = -1
        result = test_function(cards, query)
        self.assertEqual(result, output)

    def test_repeats(self):
        cards = [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
        query = 3
        output = 7
        result = test_function(cards, query)
        self.assertEqual(result, output)

    def test_query_repeats(self):
        cards = [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
        query = 6
        output = [2, 3, 4, 5, 6]
        result = test_function(cards, query)
        self.assertIn(result, output)

    def test_large_data(self):
        cards = list(range(10000000, 0, -1))
        query = 2
        output = 9999998
        result = test_function(cards, query)
        self.assertEqual(result, output)


if __name__ == "__main__":
    # Run the test
    unittest.main()
