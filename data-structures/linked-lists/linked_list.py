from node import Node


class LinkedList:
    def __init__(self, iter=[]):
        self.head = None
        self._size = 0

    def __repr__(self):
        return 'head => {}'.format(self.head.val)

    def __len__(self):
        return self._size

    def insert(self, val):
        self.head = Node(val, self.head)
        self._size += 1

    def find(self, val):
        current = self.head
        while current:
            if val == current.val:
                return True
            current = current._next
        return False