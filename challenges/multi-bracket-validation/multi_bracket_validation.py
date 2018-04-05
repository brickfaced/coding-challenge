class Node:
    """
    Create a Node to be inserted into our linked list
    """
    def __init__(self, val, next=None):
        """
        Initializes our node
        """
        self.val = val
        self.next = next

    def __repr__(self, val):
        """
        Displays the value of the node
        """
        return '{val}'.format(val=self.val)


class Stack:
    def __init__(self, iter=[]):
        self.top = None
        self._height = 0

        for item in iter:
            self.push(item)

    def __repr__(self):
        """
        Returns a string that contains the value of the top of the stack
        """
        if self._height == 0:
            return 'Stack is empty'

        return 'Top of stack is {}'.format(self.top.val)

    def __str__(self):
        """
        Returns the value of the top of the stack
        """
        if self._height == 0:
            return 'Stack is empty'

        return self.top.val

    def __len__(self):
        return self._height

    def peek(self):
        """
        Returns the value of the top of the stack
        """
        return self.top.val

    def push(self, val):
        """
        Pushes a new value at the top of the stack
        """
        self.top = Node(val, self.top)
        self._height += 1

    def pop(self):
        """
        Removes the value at the top of the stack and sets the next value
        as the new top
        """
        if len(self) == 0:
            raise IndexError('Stack is empty')

        temp = self.top
        self.top = temp.next
        self._height -= 1
        return temp.val


def multi_bracket_validation(string):
    """
    Validates if each bracket has a pair
    """
    if isinstance(string, str) is False:
        raise TypeError('Input is not a string')

    brackets = {'(': ')', '{': '}', '[': ']'}
    balance = Stack()

    for i in string:

        if i in brackets.keys():
            balance.push(i)

        if i in brackets.values():
            if balance.top is None:
                return False

            elif brackets[balance.top.val] == i:
                balance.pop()

    if len(balance) == 0:
        return True

    return False
