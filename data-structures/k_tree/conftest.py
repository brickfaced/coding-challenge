import pytest
from .k_tree import KTree as KT


@pytest.fixture
def empty_kt():
    return KT()


@pytest.fixture
def predefined_kt():
    ramon = KT()
    ramon.insert(1)
    ramon.insert(2, 1)
    ramon.insert(3, 1)
    ramon.insert(4, 3)
    ramon.insert(5, 3)
    return ramon


@pytest.fixture
def non_unique_kt():
    ramon = KT()
    ramon.insert(1)
    ramon.insert(2, 1)
    ramon.insert(2, 1)
    ramon.insert(4, 2)
    ramon.insert(5, 4)
    ramon.insert(2, 5)
    return ramon
