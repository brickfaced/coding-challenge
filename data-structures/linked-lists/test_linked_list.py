from linked_list import LinkedList as LL
import pytest


def test_insert_first_node(empty_ll):
    assert empty_ll.head is None
    empty_ll.insert(2)
    assert empty_ll.head.val == 2


def test_find_an_int_in_ll(predefined_ll):
    assert predefined_ll.find(1) is True
    assert predefined_ll.find(11) is False


def test_noniterable_as_argument():
    with pytest.raises(TypeError):
        LL(1234)


def test_append_node_on_empty(empty_ll):
    assert empty_ll.find(2) is False
    empty_ll.append(2)
    assert empty_ll.find(2) is True


def test_append_node_on_ll(predefined_ll):
    assert predefined_ll.find(11) is False
    assert predefined_ll.len() == 10
    predefined_ll.append(11)
    assert predefined_ll.find(11) is True
    assert predefined_ll.len() == 11


def test_nonvalue_as_argument(empty_ll):
    with pytest.raises(TypeError):
        empty_ll.append()


def test_insert_before(predefined_ll):
    assert predefined_ll.head._next.val == 2
    predefined_ll.insert_before(2, 11)
    assert predefined_ll.head._next.val == 11


def test_insert_after(predefined_ll):
    assert predefined_ll.head._next.val == 2
    predefined_ll.insert_after(1, 11)
    assert predefined_ll.head._next.val == 11
