"""Doubly Linked List"""
from typing import Any, Optional, Iterable


class Node:
    """Node class for the doubly linked list"""
    def __init__(self, val, next_node, prev_node):
        self.val = val
        self.next_node = next_node
        self.prev_node = prev_node

    def __repr__(self):
        if self.next_node is None:
            return f"{self.val}"
        return f"{self.val} <--> {self.next_node}"

class DoublyLinkedList:
    """Doubly Linked List Class"""
    def __init__(self, iterable: Optional[Iterable] = None):
        self.head = None
        self.tail = None
        self.length = 0
        if isinstance(iterable, (list, tuple, str)):
            for item in iterable:
                self.push(item)

    def __repr__(self):
        if self.length == 0:
            return f"Your Doubly Linked List is empty"
        elif self.head.next_node is None:
            return f"{self.head.val}"
        return f"{self.head.val} <--> {self.head.next_node}"

    def __len__(self):
        return self.length

    def push(self, val):
        self.head = Node(val, self.head, None)
        self.length += 1
        if self.length == 1:
            self.tail = self.head
        else:
            self.head.next_node.prev_node = self.head

    def append(self, val):
        self.tail = Node(val, None, self.tail)
        self.length += 1
        if self.length == 1:
            self.head = self.tail
        else:
            self.tail.prev_node.next_node = self.tail

    def pop(self):
        if self.length == 0:
            raise IndexError("Cannot pop from an empty list")
        output = self.head.val
        self.head = self.head.next_node
        self.head.prev_node = None
        self.length -= 1
        return output

    def shift(self):
        if self.length == 0:
            raise IndexError("Cannot shift from an empty list")
        output = self.tail.val
        self.tail = self.tail.prev_node
        self.tail.next_node = None
        self.length -= 1
        return output

    def remove(self, val):
        current_node = self.head
        while current_node.val != val:
            current_node = current_node.next_node
            if current_node is None:
                raise ValueError("Value does not exist in list")
        if current_node == self.head:
            self.head = self.head.next_node
            self.head.prev_node = None
            self.length -= 1
            return self
        elif current_node == self.tail:
            self.tail = self.tail.prev_node
            self.tail.next_node = None
            self.length -= 1
            return self
        else:
            current_node.prev_node.next_node = current_node.next_node
            current_node.next_node.prev_node = current_node.prev_node
            self.length -= 1
            return self
