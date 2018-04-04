from queue.node import Node


class AnimalShelter:
    def __init__(self, iter=[]):
        self.front = None
        self.back = None
        self._length = 0

        for item in iter:
            self.enqueue(item)

    def __len__(self):
        return self._length

    def __repr__(self):
        """
        Returns the front value of the queue
        """
        if self.front is None:
            return 'Queue is empty'

        return 'First in queue is: {}'.format(self.front.val)

    def __str__(self):
        """
        Returns the back of the queue
        """
        if self.back is None:
            return 'Queue is empty'

        return 'Back of queue is: {}'.form(self.back.val)

    def enqueue(self, val):
        """
        Adds animal to the back of the queue
        """
        node = Node(val)

        if len(self) == 0:
            self.back = self.front = node
            self._length += 1
            return node

        self.back.next = node
        self.back = node
        self._length += 1

    def dequeue(self, pref):
        """
        Moves the front of the queue out and moves the next value to the front
        """
        if len(self) == 0:
            raise IndexError('Queue is empty')

        current = self.front

        while current.val != pref:
            current = current.next

        return current
