from node import Node


class LinkedList:
    def __init__(self, iter=[]):
        """
        Initializes a singly linked list
        """
        self.head = None
        self._size = 0
        if type(iter) not in [str, tuple, list]:
            raise TypeError('Please pass an iterable')

        for item in reversed(iter):
            self.insert(item)

    def __repr__(self):
        """
        Returns a string that contains the value of the top of the stack
        """
        if self._size == 0:
            return 'Linked List is empty'

        return 'Head is {}'.format(self.head.val)

    def __str__(self):
        """
        Returns the value of the top of the stack
        """
        if self._size == 0:
            return 'Linked List is empty'

        return self.top.val

    def __len__(self):
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

    def append(self, val):
        """
        Inserts value to end of linked list
        """
        if type(val) is None:
            raise TypeError('Please insert pass in a value as an argument')

        if self._size == 0:
            self.insert(val)
            return

        current = self.head
        while current._next:
            current = current._next

        current._next = Node(val)
        self._size += 1

    def insert_before(self, loc, val):
        """
        Inserts a value before a given value in the linked list
        """
        current = self.head
        while current._next.val != loc:
            current = current._next

        current._next = Node(val, current._next)
        self._size += 1

    def insert_after(self, loc, val):
        """
        Inserts a value after a given value in the linked list
        """
        current = self.head
        while current.val != loc:
            current = current._next

        current._next = Node(val, current._next)
        self._size += 1

    def kth_from_end(self, k):
        """
        Returns the node at "k"s distance from the end of the linked list
        """
        if k > len(self):
            raise ValueError('k exceeds the length of this linked list')

        current = self.head
        counter = 0
        while counter != len(self) - (k + 1):
            current = current._next
            counter += 1
        return current

    def find_loop(self):
        if self.head is None:
            raise ValueError('Make sure linked list has nodes')

        current = self.head
        counter = 0

        while current._next:
            if counter > len(self):
                return True

            current = current._next
            counter += 1

        return False
