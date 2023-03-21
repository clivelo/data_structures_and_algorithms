# Dealing with collision with Linear Probing
class HashTable:
    MAX_HASH_TABLE_SIZE = 4096

    def __init__(self):
        self.data = [None] * HashTable.MAX_HASH_TABLE_SIZE

    def insert(self, key, value):
        self.data[self.hash(key)] = (key, value)

    def find(self, key):
        kv = self.data[self.hash(key)]
        return None if kv is None else kv[1]

    def update(self, key, value):
        self.data[self.hash(key)] = (key, value)

    def list_all(self):
        return [kv[0] for kv in self.data if kv is not None]

    def hash(self, key):
        idx = 0
        for char in key:
            idx += ord(char)

        idx = idx % HashTable.MAX_HASH_TABLE_SIZE

        idx = self.linear_probing(idx, key)
        return idx

    def linear_probing(self, idx, key):
        while True:
            if self.data[idx] is None:
                return idx

            k, v = self.data[idx]
            if key == k:
                return idx

            idx += 1
            if idx == HashTable.MAX_HASH_TABLE_SIZE:
                idx = 0
