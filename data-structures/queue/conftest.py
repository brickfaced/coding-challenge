import pytest
from queue.queue import Queue as Q
from queue.fifo_animal_shelter import AnimalShelter as AS

@pytest.fixture
def empty_q():
    return Q()


@pytest.fixture
def predefined_q():
    return Q([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


@pytest.fixture
def empty_as():
    return AS()


@pytest.fixture
def predefined_as():
    return AS(['cat', 'dog', 'cat', 'dog'])
