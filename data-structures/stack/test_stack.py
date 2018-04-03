from stack.stack import Stack
import pytest


def test_push(empty_stack):
    assert empty_stack.top is None
    empty_stack.push(1)
    assert empty_stack.top.val == 1


def test_pop(predefined_stack):
    assert predefined_stack.top.val == 10
    predefined_stack.pop()
    assert predefined_stack.top.val == 9


def test_pop_on_empty_stack(empty_stack):
    with pytest.raises(IndexError):
        empty_stack.pop()
