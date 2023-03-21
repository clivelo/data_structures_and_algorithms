import unittest
from ..hash_table import HashTable


class UnitTestCase(unittest.TestCase):

    def test_size(self):
        hash_table = HashTable()
        self.assertEqual(len(hash_table.data), HashTable.MAX_HASH_TABLE_SIZE, "test_size")

    def test_insert_find(self):
        hash_table = HashTable()
        hash_table.insert("Johnny Chan", 323)
        hash_table.insert("Patrick Levon", 495)
        self.assertEqual(hash_table.find("Patrick Levon"), 495, "test_insert_find")

    def test_update(self):
        hash_table = HashTable()
        hash_table.insert("Johnny Chan", 323)
        hash_table.insert("Patrick Levon", 495)
        hash_table.update("Patrick Levon", 928)
        self.assertEqual(hash_table.find("Patrick Levon"), 928, "test_update")

    def test_list_all(self):
        hash_table = HashTable()
        hash_table.insert("Johnny Chan", 323)
        hash_table.insert("Patrick Levon", 495)
        self.assertEqual(hash_table.list_all(), ["Johnny Chan", "Patrick Levon"], "test_list_all")

    def test_collision_values(self):
        hash_table = HashTable()
        hash_table.insert("listen", 99)
        hash_table.insert("silent", 200)
        self.assertTrue(hash_table.find("listen") == 99 and hash_table.find("silent") == 200, "test_collision_values")

    def test_collision_update(self):
        hash_table = HashTable()
        hash_table.insert("listen", 99)
        hash_table.insert("silent", 200)
        hash_table.insert("listen", 101)
        self.assertTrue(hash_table.find("listen") == 101 and hash_table.find("silent") == 200, "test_collision_update")

    def test_collision_list_all(self):
        hash_table = HashTable()
        hash_table.insert("listen", 99)
        hash_table.insert("silent", 200)
        self.assertEqual(hash_table.list_all(), ["listen", "silent"], "test_collision_list_all")


if __name__ == "__main__":
    unittest.main()
