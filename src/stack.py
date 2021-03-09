"""Stack"""
from typing import Any, Optional, Iterable


class Node:
    """Node class for the stack"""
    def __init__(self, val: Any, next_node: "Node"):
        self.val = val
        self.next_node = next_node

    def __repr__(self):
        return f"{self.val} \n" \
               f"{self.next_node}"

class Stack:
    """Stack class"""
    def __init__(self, iterable: Optional[Iterable] = None):
        self._top = None
        self._size = 0
        if isinstance(iterable, (list, tuple, str)):
            for item in iterable:
                self.push(item)
        elif iterable is not None:
            raise TypeError("If providing an input, it must be an iterable.")

    def __repr__(self):
        if self._top is None:
            return f"Your Stack is empty"
        return f"{self._top.val} \n" \
               f"{self._top.next_node}"

    def __len__(self):
        return self._size

    def top(self):
        return self._top

    # def is_empty(self):

    # def size(self):

    def push(self, val):
        self._top = Node(val, self._top)
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise IndexError("Your Stack is empty - nothing to pop here")
        popped_value = self._top.val
        self._top = self._top.next_node
        self._size -= 1
        return popped_value
