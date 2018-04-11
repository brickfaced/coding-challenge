from .stacks import Stack


class Queue:
    def __init__(self, iter=[]):
        """
        Instantiates a queue with stacks
        """
        self.size = 0
        self.stack_one = Stack()
        self.stack_two = Stack()

        for item in iter:
            self.enqueue(item)

    def enqueue(self, val):
        """
        Inserts a value(s) into stack_one
        """
        self.stack_one.push(val)
        self.size += 1

    def dequeue(self):
        """
        Inserts all the values from stack_one
        into stack_two and returns the last value inserted.
        Then it adds all the values back into
        stack_one from stack_two except the returned value.
        Finally it decrements the size of the queue
        """
        if self.size == 0:
            raise IndexError('Nothing to dequeue')

        while self.stack_one._height != 0:
            self.stack_two.push(self.stack_one.pop())

        self.size -= 1
        dequeued_val = self.stack_two.pop()

        while self.stack_two._height != 0:
            self.stack_one.push(self.stack_two.pop())

        return dequeued_val
