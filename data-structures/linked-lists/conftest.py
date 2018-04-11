import pytest
from linked_list import LinkedList as LL


@pytest.fixture
def empty_ll():
    return LL()


@pytest.fixture
def predefined_ll():
    return LL([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


@pytest.fixture
def predefined_ll_two():
    return LL([1, 2, 3, 4, 5])


@pytest.fixture
def predefined_ll_three():
    return LL([6, 7, 8, 9])
