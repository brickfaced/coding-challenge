import pytest
from stack.stack import Stack as S


@pytest.fixture
def empty_stack():
    return S()


@pytest.fixture
def predefined_stack():
    return S([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])