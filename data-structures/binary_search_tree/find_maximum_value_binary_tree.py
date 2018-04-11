def find_maximum_value(bst):
    """
    Takes in a binary search tree goes through
    each value and returns the highest value
    inside the binary search tree
    """
    values = []
    bst.pre_order(lambda node: values.append(node.val))
    current_max = 0
    for i in range(len(values)):
        if values[i] > current_max:
            current_max = values[i]

    return current_max
