from linked_list import LinkedList as LL


class HashTable:
    def __init__(self, max_size=1024):
        self.max_size = max_size
        self.buckets = [LL() for _ in range(self.max_size)]

    def hash_key(self, key):
        if type(key) is not str:
            raise TypeError

        sum = 0
        for char in key:
            sum += ord(char)

        return sum % len(self.buckets)

    def _set(self, key, val):
        if self.buckets[self.hash_key(key)]:
            return self.buckets[self.hash_key(key)].append({key: val})

        return self.buckets[self.hash_key(key)].insert({key: val})

    def get(self, key):
        if len(self.buckets[self.hash_key(key)]) > 1:
            return self.buckets[self.hash_key(key)].find(key)

        return self.buckets[self.hash_key(key)]

    def remove(self, key):
        if len(self.buckets[self.hash_key(key)]) > 1:
            temp = self.buckets[self.hash_key(key)].find(key)
            self.buckets[self.hash_key(key)].find(key).val = None
            return temp

        temp = self.buckets[self.hash_key(key)]
        self.buckets[self.hash_key(key)] = None
        return temp
