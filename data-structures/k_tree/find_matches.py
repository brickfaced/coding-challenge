"""Search to see if the value you want is inside a ktree."""


def find_matches(ktree, val):
    """Search for values and append to your collection."""
    collection = []

    ktree.pre_order(lambda n: collection.append(n) if n.val == val else None)

    if collection == []:
        raise ValueError('Your value did not match any values in the tree')

    return collection
