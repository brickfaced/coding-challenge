from .bst import BST
import pytest
from .fizzbuzztree import fizzbuzztree


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


def test_fizzbuzztree(predefined_bst_two):
    pre_fizzbuzz = []
    post_fizzbuzz = []
    predefined_bst_two.in_order(lambda n: pre_fizzbuzz.append(n.val))
    assert pre_fizzbuzz == [1, 2, 3, 4, 5, 15, 30]
    predefined_bst_two.in_order(fizzbuzztree)
    predefined_bst_two.in_order(lambda n: post_fizzbuzz.append(n.val))
    assert post_fizzbuzz == [1, 2, 'Fizz', 4, 'Buzz', 'FizzBuzz', 'FizzBuzz']
