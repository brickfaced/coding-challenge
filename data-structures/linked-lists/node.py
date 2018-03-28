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
