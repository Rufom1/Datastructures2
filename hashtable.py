

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False
    

    def exists(self, key):
        index = self._hash(key)
        for k in self.table[index]:
            if k == key:
                return True
        return False
    

if __name__ == "__main__":
    # Example usage
    ht = HashTable()
    ht.insert("key1", "value1")
    ht.insert("key2", "value2")
    print(ht.get("key1"))  # Output: value1
    print(ht.exists("key2"))  # Output: True
    ht.remove("key1")
    print(ht.get("key1"))  # Output: None
    print(ht.exists("key1"))  # Output: False