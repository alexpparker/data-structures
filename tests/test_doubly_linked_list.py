"""Test Doubly Linked List Implementation"""
import pytest
from doubly_linked_list import DoublyLinkedList


@pytest.fixture
def new_dll():
    return DoublyLinkedList()


def test_dll_head_and_tail(new_dll):
    """Tests that a new DLL has a head&tail --> None and length is 0"""
    assert hasattr(new_dll, "head")
    assert hasattr(new_dll, "tail")
    assert new_dll.head is None
    assert new_dll.tail is None
    assert len(new_dll) == 0


@pytest.mark.parametrize('iterable', [
    ["1", "2", "3"],
    ("1", "2", "3"),
    "123"
])
def test_dll_iterable_input(iterable):
    new_dll = DoublyLinkedList(iterable)
    assert new_dll.head.val == "3"
    assert new_dll.head.next_node.val == "2"
    assert new_dll.tail.prev_node.val == "2"
    assert new_dll.tail.val == "1"


@pytest.mark.parametrize('num_list', [
    [1],
    [1, 2],
    [1, 2, 3],
    list(range(20)),
    list(range(40)),
    list(range(3)),
    list(range(10))
])
def test_dll_length(num_list):
    new_dll = DoublyLinkedList(num_list)
    assert len(new_dll) == len(num_list)


def test_push_method(new_dll):
    new_dll.push(5)
    assert new_dll.head.val == 5
    new_dll.push(4)
    assert new_dll.head.val == 4


def test_append_method(new_dll):
    new_dll.append(5)
    assert new_dll.tail.val == 5
    new_dll.append(4)
    assert new_dll.tail.val == 4


def test_pop_returns_whatever_is_in_head():
    new_dll = DoublyLinkedList([1, 2, 3])
    assert new_dll.pop() == 3
    assert new_dll.head.val == 2


def test_pop_empty_raises_index_error():
    new_dll = DoublyLinkedList()
    with pytest.raises(IndexError):
        new_dll.pop()


def test_shift_tail():
    new_dll = DoublyLinkedList([1, 2, 3])
    new_dll.shift()
    assert new_dll.tail.val == 2


def test_shift_empty_raises_index_error():
    new_dll = DoublyLinkedList()
    with pytest.raises(IndexError):
        new_dll.shift()


def test_remove_value():
    new_dll = DoublyLinkedList([1, 2, 3, 4, 5])
    assert len(new_dll.remove(3)) == 4
    assert new_dll.head.next_node.val == 4
    assert new_dll.head.next_node.next_node.val == 2


def test_remove_value_error():
    new_dll = DoublyLinkedList([1, 2, 3, 4, 5])
    with pytest.raises(ValueError):
        new_dll.remove(6)
