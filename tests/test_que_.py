"""Tests for Queue Implementation"""
import pytest
from que_ import Queue


@pytest.fixture
def new_queue():
    return Queue()


def test_empty_queue_init(new_queue):
    assert new_queue.front is None
    assert new_queue.back is None
    assert len(new_queue) == 0


@pytest.mark.parametrize("iterable", [
    ["1", "2", "3"],
    ("1", "2", "3"),
    "123"
])
def test_iterable_queue_init(iterable):
    new_queue = Queue(iterable)
    assert new_queue.front.val == "1"
    assert new_queue.back.val == "3"
    assert new_queue.back.next_node.val == "2"
    assert len(new_queue) == 3


def test_improper_init():
    with pytest.raises(TypeError):
        new_queue = Queue(4)


@pytest.mark.parametrize("num_list", [
    [1],
    [1, 2],
    [1, 2, 3],
    list(range(20)),
    list(range(40)),
    list(range(3)),
    list(range(10))
])
def test_len_function(num_list):
    new_queue = Queue(num_list)
    assert len(new_queue) == len(num_list)


def test_enqueue_on_empty_queue(new_queue):
    new_queue.enqueue(4)
    assert new_queue.back.val == 4
    assert new_queue.front.val == 4
    assert len(new_queue) == 1


def test_enqueue_on_non_empty_queue():
    new_queue = Queue("234")
    new_queue.enqueue(5)
    assert new_queue.back.val == 5
    assert new_queue.front.val == "2"
    assert len(new_queue) == 4


def test_dequeue_on_empty_queue(new_queue):
    with pytest.raises(IndexError):
        new_queue.dequeue()


def test_dequeue_on_single_entry_queue():
    new_queue = Queue("a")
    new_queue.dequeue()
    assert new_queue.back is None
    assert new_queue.front is None
    assert len(new_queue) == 0


def test_dequeue_on_double_entry_queue():
    new_queue = Queue("sd")
    new_queue.dequeue()
    assert new_queue.back.val == "d"
    assert new_queue.front.val == "d"
    assert new_queue.back.next_node is None
    assert len(new_queue) == 1


def test_dequeue_on_multi_entry_queue():
    new_queue = Queue("asddfafsadsa")
    for i in range(4):
        new_queue.dequeue()
    assert len(new_queue) == len("asddfafsadsa") - 4
    assert new_queue.back.val == "a"
    assert new_queue.front.val == "f"


def test_peek_on_empty_queue(new_queue):
    with pytest.raises(IndexError):
        new_queue.peek()


def test_peek_on_single_entry_queue():
    new_queue = Queue("4")
    assert new_queue.peek() == "4"


def test_peek_on_multi_entry_queue():
    new_queue = Queue("sdfg")
    assert new_queue.peek() == "s"
