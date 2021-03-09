"""Queue"""
from typing import Any, Optional, Iterable


class Node:
    def __init__(self, val, next_node):
        self.val = val
        self.next_node = next_node

    def __repr__(self):
        if self.next_node is None:
            return f"{self.val}"
        return f"{self.val} -> {self.next_node}"


class Queue:
    def __init__(self, iterable: Optional[Iterable] = None):
        self.front = None
        self.back = None
        self.length = 0
        if isinstance(iterable, (list, tuple, str)):
            for item in iterable:
                self.enqueue(item)
        elif iterable is not None:
            raise TypeError("If providing an input, it must be an iterable")

    def __len__(self):
        return self.length

    def __repr__(self):
        if self.length == 0:
            return f"Your Queue is empty"
        if self.back.next_node is None:
            return f"{self.back.val}"
        return f"{self.back.val} -> {self.back.next_node}"

    def enqueue(self, val):
        if self.length == 0:
            self.back = Node(val, None)
            self.front = self.back
            self.length += 1
        else:
            self.back = Node(val, self.back)
            self.length += 1

    def dequeue(self):
        if self.length == 0:
            raise IndexError("Your queue is empty - nothing to dequeue here!")
        output = self.front.val
        if self.length == 1:
            self.back = None
            self.front = None
            self.length -= 1
            return output
        if self.length == 2:
            self.back.next_node = None
            self.front = self.back
            self.length -= 1
            return output
        next_in_line = self.back.next_node
        while next_in_line.next_node.next_node is not None:
            next_in_line = next_in_line.next_node
        self.front = next_in_line
        next_in_line.next_node = None
        self.length -= 1
        return output

    def peek(self):
        if self.length == 0:
            raise IndexError("Your queue is empty - nothing to dequeue here!")
        return self.front.val
