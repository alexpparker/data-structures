"""Test the stack implementation"""
import pytest
from stack import Stack


def test_stack_head():
    """Tests that a new Stack has a top"""
    new_stack = Stack()
    assert hasattr(new_stack, "_top")
    assert new_stack._top is None


def test_stack_push_val():
    """When a value is pushed on an empty stack, it is the top"""
    new_stack = Stack()
    new_stack.push(5)
    assert new_stack._top.val == 5


def test_stack_push_two():
    """When I push two values, both are in the stack and the last one is the head"""
    new_stack = Stack()
    new_stack.push(5)
    new_stack.push(3)
    assert new_stack._top.val == 3
    assert new_stack._top.next_node.val == 5


@pytest.mark.parametrize('iterable', [
    ["1", "2", "3"],
    ("1", "2", "3"),
    "123"
])
def test_stack_with_iterable_inserts_every_value(iterable):
    """."""
    new_stack = Stack(iterable)
    assert new_stack._top.val == "3"
    assert new_stack._top.next_node.val == "2"
    assert new_stack._top.next_node.next_node.val == "1"


def test_stack_with_noniterable_raises_exception():
    """."""
    with pytest.raises(TypeError):
        Stack(4)


def test_pop_returns_whatever_is_on_top():
    new_stack = Stack([1, 2, 3])
    assert new_stack.pop() == 3
    assert new_stack._top.val == 2


def test_pop_empty_raises_index_error():
    new_stack = Stack()
    with pytest.raises(IndexError):
        new_stack.pop()


@pytest.mark.parametrize('num_list', [
[1],
    [1, 2],
    [1, 2, 3],
    list(range(20)),
    list(range(40)),
    list(range(3)),
    list(range(10))
])
def test_can_get_size_of_stack(num_list):
    new_stack = Stack(num_list)
    assert len(new_stack) == len(num_list)