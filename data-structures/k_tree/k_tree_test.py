"""Welcome to the KTree Testing Zone."""
from .print_level_order import print_level_order as plo
from .find_matches import find_matches as fm
import pytest


def test_ktree_insert(empty_kt):
    """Tests to see if the insert method works as expected."""
    empty_kt.insert(1)
    assert empty_kt.root.val == 1
    empty_kt.insert(2, 1)
    assert empty_kt.root.children[0].val == 2
    empty_kt.insert(3, 1)
    assert empty_kt.root.children[1].val == 3


def test_ktree_pre_order(predefined_kt):
    """Tests to see if the ktree is being traversed correctly."""
    order = []
    predefined_kt.pre_order(lambda n: order.append(n.val))
    assert order == [1, 2, 3, 4, 5]


def test_ktree_post_order(predefined_kt):
    """Tests to see if the ktree is being traversed correctly."""
    order = []
    predefined_kt.post_order(lambda n: order.append(n.val))
    assert order == [2, 4, 5, 3, 1]


def test_ktree_breadth_first_order(predefined_kt):
    """Tests to see if the ktree is being traversed correctly."""
    order = []
    predefined_kt.breadth_first_traversal(lambda n: order.append(n.val))
    assert order == [1, 2, 3, 4, 5]


def test_print_level_order(predefined_kt, empty_kt):
    """Tests to see if there is a newline in ever level of ktree."""
    assert plo(predefined_kt) == '1\n23\n45\n'
    with pytest.raises(ValueError):
        plo(empty_kt)


def test_find_matches(non_unique_kt):
    """Tests to see if all matches are found."""
    assert [node.val for node in fm(non_unique_kt, 2)] == [2, 2, 2]
    non_unique_kt.insert(2, 1)
    assert [node.val for node in fm(non_unique_kt, 2)] == [2, 2, 2, 2]


def test_find_no_matches(non_unique_kt):
    """Tests to see if ValueError gets raised."""
    with pytest.raises(ValueError):
        fm(non_unique_kt, 24)
