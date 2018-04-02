from queue.queue import Queue
import pytest


def test_enqueue(empty_q):
    assert empty_q.front is None
    empty_q.enqueue(1)
    assert empty_q.front.val == 1


def test_dequeue(predefined_q):
    assert predefined_q.front.val == 1
    predefined_q.dequeue()
    assert predefined_q.front.val == 2


def test_dequeue_on_empty_q(empty_q):
    with pytest.raises(IndexError):
        empty_q.dequeue()
