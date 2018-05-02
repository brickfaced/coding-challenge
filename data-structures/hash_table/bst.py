class Node:
    def __init__(self, val):
        """
        Instantiates a node
        """
        self.val = val
        self.right = None
        self.left = None

    def __repr__(self):
        """
        Prints out the nodes value
        """
        return '<Node Val: {}'.format(self.val)

    def __str__(self):
        """
        Outputs the current nodes value
        """
        return str(self.val)


class BST:
    def __init__(self, iter=[]):
        """
        Instantiates a binary search tree using an iterable of integers
        """
        self.root = None

        if not isinstance(iter, (list, dict, tuple)):
            raise TypeError('Please pass an iterable')

        for item in iter:
            self.insert(item)

    def __repr__(self):
        """
        Prints out the roots value
        """
        return '<BST Root {}>'.format(self.root.val)

    def __str__(self):
        """
        Outputs the roots value
        """
        return self.root.val

    def insert(self, val):
        """
        Inserts a node depending on it's numerical order.
        """
        node = Node(val)
        current = self.root

        if self.root is None:
            self.root = node
            return node

        while current:
            if val >= current.val:
                if current.right is not None:
                    current = current.right

                else:
                    current.right = node
                    break

            elif val < current.val:
                if current.left is not None:
                    current = current.left

                else:
                    current.left = node
                    break

        return node

    def in_order(self, operation):
        """
        Traverses through the BST in order
        """
        def _walk(node=None):
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)

            operation(node)

            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def pre_order(self, operation):
        """
        Traverses through the BST pre order
        """
        def _walk(node=None):
            if node is None:
                return

            operation(node)

            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def post_order(self, operation):
        """
        Traverses through the BST post order
        """
        def _walk(node=None):
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)

            operation(node)

        _walk(self.root)
