class HashTable:
    def __init__(self):
        self.collection = dict()

    def hash(self, txt):
        return sum(ord(c) for c in txt)

    def add(self, key, value):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            self.collection[hashed_key] = dict()
        self.collection[hashed_key][key] = value

    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                del self.collection[hashed_key][key]
            else:
                del self.collection[hashed_key]

    def lookup(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            return self.collection[hashed_key].get(key, None)
        return self.collection.get(hashed_key, None)

    def __str__(self):
        return str(self.collection)


ht = HashTable()
print("---\n")
print(ht.hash("golf"))
ht.add("golf", "sport")
ht.add("dear", "friend")
ht.add("read", "book")
# ht.add('rose', 'flower')
print(ht)
print(ht.lookup("golf"))
ht.remove("read")
print(ht)
print(ht.lookup("read"))
