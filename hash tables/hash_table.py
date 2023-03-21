class HashTable:
    MAX_HASH_TABLE_SIZE = 4096

    def __init__(self):
        self.data = [None] * HashTable.MAX_HASH_TABLE_SIZE

    def insert(self, key, value):
        self.data[HashTable.hash(key)] = (key, value)

    def find(self, key):
        kv = self.data[HashTable.hash(key)]
        return None if kv is None else kv[1]

    def update(self, key, value):
        self.data[HashTable.hash(key)] = (key, value)

    def list_all(self):
        return [kv[0] for kv in self.data if kv is not None]

    @classmethod
    def hash(cls, key):
        result = 0
        for char in key:
            result += ord(char)

        return result % cls.MAX_HASH_TABLE_SIZE
