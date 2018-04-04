from queue.fifo_animal_shelter import AnimalShelter as AS
import pytest


def test_enqueue(empty_as):
    assert empty_as.front is None
    empty_as.enqueue('cat')
    assert empty_as.front.val == 'cat'


def test_dequeue(predefined_as):
    assert predefined_as.front.val == 'cat'
    assert predefined_as.dequeue('cat').val == 'cat'
