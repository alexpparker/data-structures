"""Test the linked_list implementation."""
import pytest
import random
from linked_list import LinkedList

PARAMS_TABLE = [
    [1],
    [1, 2],
    [1, 2, 3],
    list(range(20)),
    list(range(40)),
    list(range(3)),
    list(range(10))
]


def test_linked_list_head():
    """Tests that a new LinkedList has a head"""
    new_list = LinkedList()
    assert hasattr(new_list, "head")


def test_linked_list_head_is_none():
    """Tests that the value of a new LinkedList head is None"""
    new_list = LinkedList()
    assert new_list.head is None


def test_linked_list_push_val():
    """When a value is pushed on an empty list, it is the head"""
    new_list = LinkedList()
    new_list.push(5)
    assert new_list.head.val == 5


def test_linked_list_push_two():
    """When I push two values, both are in the list and the last one is the head"""
    new_list = LinkedList()
    new_list.push(4)
    new_list.push(5)
    assert new_list.head.val == 5
    assert new_list.head.next_node.val == 4


def test_linked_list_with_list_inserts_every_value():
    """."""
    new_list = LinkedList([1, 2, 3])
    assert new_list.head.val == 3
    assert new_list.head.next_node.val == 2
    assert new_list.head.next_node.next_node.val == 1


def test_linked_list_with_tuple_inserts_every_value():
    """."""
    new_list = LinkedList((1, 2, 3))
    assert new_list.head.val == 3
    assert new_list.head.next_node.val == 2
    assert new_list.head.next_node.next_node.val == 1


def test_linked_list_with_str_inserts_every_value():
    """."""
    new_list = LinkedList("abc")
    assert new_list.head.val == "c"
    assert new_list.head.next_node.val == "b"
    assert new_list.head.next_node.next_node.val == "a"


def test_linked_list_with_noniterable_raises_exception():
    """."""
    with pytest.raises(TypeError):
        LinkedList(5)


def test_pop_returns_whatever_is_in_head():
    new_list = LinkedList([1, 2, 3])
    assert new_list.pop() == 3


def test_pop_empty_raises_index_error():
    new_list = LinkedList()
    with pytest.raises(IndexError):
        new_list.pop()


@pytest.mark.parametrize('num_list', PARAMS_TABLE)
def test_can_get_length_of_list(num_list):
    new_list = LinkedList(num_list)
    assert len(new_list) == len(num_list)
