
class Node:
    def __init__(self, val, children=[]):
        """
        Instantiates a node for KTree
        """
        self.val = val
        self.children = children

    def __repr__(self):
        """
        Prints out the nodes value
        """
        return '<Node Val: {}'.format(self.val)

    def __str__(self):
        """
        Outputs the current nodes value
        """
        return self.val


class KTree:
    def __init__(self):
        """
        Instantiates a binary search tree using a node
        """
        self.root = None

    def __repr__(self):
        """
        Prints out the roots value
        """
        return '<KTree Root {}>'.format(self.root.val)

    def __str__(self):
        """
        Outputs the roots value
        """
        return self.root.val

    def insert(self, parent, val):
        pass

    def pre_order(self, operation):
        """
        Traverses through the KTree pre order
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
        Traverses through the KTree post order
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

    def breadth_first_traversal(self):
        """
        Traverses through the KTree breadth first
        """
        nodes = [self.root]
        output = []
        while len(nodes):
            new_nodes = []
            for node in nodes:
                if node is None:
                    continue

                new_nodes.extend((node.left, node.right))
                print(node.val)
                output.append(node.val)
            nodes = new_nodes
        return output
