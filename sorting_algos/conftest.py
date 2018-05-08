import pytest


@pytest.fixture
def small_lst():
    return [1]


@pytest.fixture
def uneven_lst():
    return [100, 24, 11, 72, 7, 30]


@pytest.fixture
def reversed_lst():
    return [5, 4, 3, 2, 1]
