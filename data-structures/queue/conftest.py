import pytest
from queue.queue import Queue as Q


@pytest.fixture
def empty_q():
    return Q()


@pytest.fixture
def predefined_q():
    return Q([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
