from linked_list import LinkedList as LL


class HashTable:
    def __init__(self, max_size=1024):
        """Instantiates a Hash Table"""
        self.max_size = max_size
        self.buckets = [LL() for _ in range(self.max_size)]

    def hash_key(self, key):
        """Hashes the the inserted key for a unique value"""
        if type(key) is not str:
            raise TypeError

        sum = 0
        for char in key:
            sum += ord(char)

        return sum % len(self.buckets)

    def set(self, key, val):
        if self.buckets[self.hash_key(key)]:
            return self.buckets[self.hash_key(key)].insert({key: val})

        return self.buckets[self.hash_key(key)].insert({key: val})

    def get(self, key):
        current = self.buckets[self.hash_key(key)].head
        # import pdb; pdb.set_trace()
        values = []
        while current:
            if key in current.val:
                values.append(current.val[key])

            current = current._next

        if values == []:
            return 'Key Not Found'

        return values

    def remove(self, key):
        current = self.buckets[self.hash_key(key)].head
        while current:
            if key in current.val:
                temp = current
                self.buckets[self.hash_key(key)].head = None
                return temp

            current._next

        return 'Key Not Found'
