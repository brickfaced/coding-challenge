def print_level_order(ktree):
    """
    Output each level of a KTree
    seperated by a new line
    """
    if ktree.root is None:
        raise ValueError('Please pass in a KTree with values')

    nodes = [ktree.root]
    list_of_values = []
    while len(nodes):
        new_nodes = []
        for node in nodes:
            if node is None:
                continue

            new_nodes.extend(node.children)
            print(node.val)
            list_of_values.append(node.val)

        list_of_values.append('\n')
        nodes = new_nodes

    output = ''.join(str(n) for n in list_of_values)
    return output
