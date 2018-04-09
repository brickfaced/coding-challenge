import pytest
from .bst import BST


@pytest.fixture
def predefined_bst():
    return BST([1, 2, 3, 4, 5])


@pytest.fixture
def predefined_bst_two():
    return BST([1, 2, 3, 4, 5, 15, 30])
