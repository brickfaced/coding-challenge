from node import Node


class LinkedList:
    def __init__(self, iter=[]):
        """
        Initializes a singly linked list
        """
        self.head = None
        self._size = 0
        if type(iter) not in [str, tuple, list]:
            raise TypeError('Please pass an iterable.')
        for item in reversed(iter):
            self.insert(item)

    def __repr__(self):
        """
        Displays the head of the linked list
        """
        if self.head is None:
            return 'List is empty'
        return 'head => {}'.format(self.head.val)

    def len(self):
        """
        Displays the size of the linked list
        """
        return self._size

    def insert(self, val):
        """
        Inserts a new value at the head of the linked list and increments the
        size of the linked list
        """
        self.head = Node(val, self.head)
        self._size += 1

    def find(self, val):
        """
        Takes in a value and searches for it inside the linked list and
        returns True if it is found and False if not
        """
        current = self.head
        while current:
            if val == current.val:
                return True
            current = current._next
        return False
