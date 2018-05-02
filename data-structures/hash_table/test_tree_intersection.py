"""Tree Intersection Testing Zone"""
from tree_intersection import tree_intersection as TI
from bst import BST


def test_two_trees_with_no_common_values():
    a = BST([1, 2, 3, 4])
    b = BST([5, 6, 7, 8])
    assert TI(a, b) == 'No Common Values Betweens BSTs'


def test_two_trees_with_common_values():
    a = BST([1, 2, 3, 4, 5, 6, 7, 8])
    b = BST([5, 6, 7, 8])
    assert TI(a, b) == [5, 6, 7, 8]
    b.insert(1)
    assert TI(a, b) == [5, 1, 6, 7, 8]
