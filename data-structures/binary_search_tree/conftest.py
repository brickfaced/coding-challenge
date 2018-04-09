import pytest
from .bst import BST


@pytest.fixture
def predefined_bst():
    return BST([1, 2, 3, 4, 5])
