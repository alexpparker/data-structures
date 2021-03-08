"""Singly linked list"""
from typing import Any, Optional, Iterable


class Node:
    """Node class for the linked list"""
    def __init__(self, val: Any, next_node: "Node"):
        self.val = val
        self.next_node = next_node

    def __repr__(self):
        return f"({self.val})->{self.next_node}"


class LinkedList:
    """Linked list class"""
    def __init__(self, iterable: Optional[Iterable] = None):
        self.head = None
        self._length = 0
        if isinstance(iterable, (list, tuple, str)):
            for item in iterable:
                self.push(item)
        elif iterable is not None:
            raise TypeError("If providing an input, it must be an iterable.")

    def __len__(self):
        return self._length

    def __repr__(self):
        return self.display()

    def push(self, val):
        self.head = Node(val, self.head)
        self._length += 1

    def pop(self):
        if not self.head:
            raise IndexError("Cannot pop from an empty list.")
        popped_value = self.head.val
        self.head = self.head.next_node
        self._length -= 1
        return popped_value

    def size(self):
        return self._length

    def search(self, val):
        current_node = self.head
        while current_node.val != val:
            current_node = current_node.next_node
            if current_node is None:
                break
        return current_node

    def remove(self, val):
        node = self.search(val)
        if node is None:
            raise ValueError("Value does not exist in list.")
        node.val = node.next_node.val
        node.next_node = node.next_node.next_node
        self._length -= 1
        return self

    def display(self):
        if self.head is None:
            return f"Your Linked List is empty."
        return f"({self.head.val})->{self.head.next_node}"
