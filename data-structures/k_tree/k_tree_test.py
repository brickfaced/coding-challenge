def test_ktree_insert(empty_kt):
    empty_kt.insert(1)
    assert empty_kt.root.val == 1
    empty_kt.insert(2, 1)
    assert empty_kt.root.children[0].val == 2
    empty_kt.insert(3, 1)
    assert empty_kt.root.children[1].val == 3


def test_ktree_pre_order(predefined_kt):
    order = []
    predefined_kt.pre_order(lambda n: order.append(n.val))
    assert order == [1, 2, 3, 4, 5]


def test_ktree_post_order(predefined_kt):
    order = []
    predefined_kt.post_order(lambda n: order.append(n.val))
    assert order == [2, 4, 5, 3, 1]


def test_ktree_breadth_first_order(predefined_kt):
    """Correct output order."""
    order = []
    predefined_kt.breadth_first_traversal(lambda n: order.append(n.val))
    assert order == [1, 2, 3, 4, 5]
