class Node:
    def __init__(self, val):
        """
        Instantiates a node for KTree
        """
        self.val = val
        self.children = []

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

    def insert(self, child, parent=None):
        """
        Gives a child a parent, very heartwarming stuff here
        """
        self._parent = None
        node = Node(child)
        if self.root is None:
            self.root = node
            return

        def find_parent(current):
            if current is None:
                return
            if current.val == parent:
                self._parent = current

        self.pre_order(find_parent)
        self._parent.children.append(node)

    def pre_order(self, operation):
        """
        Traverses through the KTree pre order
        """
        def _walk(node=None):
            if node is None:
                return

            operation(node)

            for children in node.children:
                _walk(children)

        _walk(self.root)

    def post_order(self, operation):
        """
        Traverses through the KTree post order
        """
        def _walk(node=None):
            if node is None:
                return

            for children in node.children:
                _walk(children)

            operation(node)

        _walk(self.root)

    def breadth_first_traversal(self, operation):
        """
        Traverses through the KTree breadth first
        """
        parents = []
        current = self.root
        parents.append(current)
        while current:
            for nodes in current.children:
                parents.append(nodes)

            operation(current)
            parents.pop(0)

            if parents == []:
                break

            current = parents[0]
