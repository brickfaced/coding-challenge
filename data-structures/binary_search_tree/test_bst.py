from .bst import BST
import pytest


def test_insert_iterable(predefined_bst):
    assert predefined_bst.root.val == 1
    assert predefined_bst.root.right.val == 2
    assert predefined_bst.root.right.right.val == 3


def test_valid_iterable():
    with pytest.raises(TypeError):
        assert BST(1234)


def test_in_order_traversal(predefined_bst):
    order = []
    predefined_bst.in_order(lambda n: order.append(n.val))
    assert order == [1, 2, 3, 4, 5]


def test_pre_order_traversal(predefined_bst):
    order = []
    predefined_bst.pre_order(lambda n: order.append(n.val))
    assert order == [1, 2, 3, 4, 5]


def test_post_order_traversal(predefined_bst):
    order = []
    predefined_bst.post_order(lambda n: order.append(n.val))
    assert order == [5, 4, 3, 2, 1]
