"""Test the linked_list implementation."""
import pytest
from linked_list import LinkedList


def test_linked_list_head():
    """Tests that a new LinkedList has a head"""
    new_list = LinkedList()
    assert hasattr(new_list, "head")
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


@pytest.mark.parametrize('iterable', [
    ["1", "2", "3"],
    ("1", "2", "3"),
    "123"
])
def test_linked_list_with_iterable_inserts_every_value(iterable):
    """."""
    new_list = LinkedList(iterable)
    assert new_list.head.val == "3"
    assert new_list.head.next_node.val == "2"
    assert new_list.head.next_node.next_node.val == "1"


def test_linked_list_with_noniterable_raises_exception():
    """."""
    with pytest.raises(TypeError):
        LinkedList(5)


def test_pop_returns_whatever_is_in_head():
    new_list = LinkedList([1, 2, 3])
    assert new_list.pop() == 3
    assert new_list.head.val == 2


def test_pop_empty_raises_index_error():
    new_list = LinkedList()
    with pytest.raises(IndexError):
        new_list.pop()


@pytest.mark.parametrize('num_list', [
    [1],
    [1, 2],
    [1, 2, 3],
    list(range(20)),
    list(range(40)),
    list(range(3)),
    list(range(10))
])
def test_can_get_length_of_list(num_list):
    new_list = LinkedList(num_list)
    assert len(new_list) == len(num_list)


def test_search_for_value():
    new_list = LinkedList([1, 2, 3, 4, 5])
    searched_node = new_list.head.next_node.next_node.next_node
    assert new_list.search(2) == searched_node


def test_search_for_missing_value():
    new_list = LinkedList([1, 2, 3, 4, 5])
    assert new_list.search(6) is None


def test_remove_value():
    new_list = LinkedList([1, 2, 3, 4, 5])
    assert len(new_list.remove(3)) == 4
    assert new_list.head.next_node.val == 4
    assert new_list.head.next_node.next_node.val == 2


def test_remove_value_error():
    new_list = LinkedList([1, 2, 3, 4, 5])
    with pytest.raises(ValueError):
        new_list.remove(6)
