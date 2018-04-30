class Node:
    """
    Create a Node to be inserted into our linked list
    """
    def __init__(self, val, next=None):
        """
        Initializes our node
        """
        self.val = val
        self._next = next

    def __repr__(self, val):
        """
        Displays the value of the node
        """
        return '{val}'.format(val=self.val)


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
        Displays the head of the linked list
        """
        if self.head is None:
            return 'List is empty'

        return 'head => {}'.format(self.head.val)

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
        returns the Node if it exists
        """
        current = self.head
        while current:
            if val == current.val:
                return current

            current = current._next

        return 'Not in Linked List'

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
