import pytest
from .stacks import Stack as S
from .queue_with_stacks import Queue


@pytest.fixture
def empty_stack():
    return S()


@pytest.fixture
def predefined_stack():
    return S([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


@pytest.fixture
def predefined_q_with_stack():
    return Queue([1, 2, 3])
