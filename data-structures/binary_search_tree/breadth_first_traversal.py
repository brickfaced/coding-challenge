def breadth_first_traversal(bst):
    nodes = [bst.root]
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
