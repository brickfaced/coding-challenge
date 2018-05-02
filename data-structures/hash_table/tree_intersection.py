from hash_table import HashTable


def tree_intersection(bst1, bst2):
    """
    Sets all values in bst1 into a hash tree
    then compares the values of bst2 to the hash tree
    If the values of bst2 are in the hash tree it will
    append into the intersected values list.
    """
    bst_values = HashTable()
    intersected_values = []
    bst1.pre_order(lambda n: bst_values._set(str(n.val), str(n.val)))
    bst2.pre_order(lambda n: intersected_values.append(n.val) if bst_values.get(str(n.val)) == str(n.val) else None)

    if intersected_values == []:
        return 'No Common Values Betweens BSTs'

    return intersected_values
