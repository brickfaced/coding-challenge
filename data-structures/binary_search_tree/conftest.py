import pytest
from .bst import BST


@pytest.fixture
def predefined_bst():
    return BST([1, 2, 3, 4, 5])


@pytest.fixture
def predefined_bst_two():
    return BST([1, 2, 3, 4, 5, 15, 30])


@pytest.fixture
def unbalanced_bst():
    return BST([15, 6, 23, 4, 7, 71, 5, 50])
