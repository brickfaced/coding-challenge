from queue.node import Node


class Queue:
    def __init__(self, iter=[]):
        self.front = None
        self.back = None
        self._length = 0

        for item in iter:
            self.enqueue(item)

    def __len__(self):
        """
        Returns the length of the queue
        """
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
        pass

    def dequeue(self):
        pass
