class Node:
    def __init__(self, val, next_node):
        self.val = val
        self.next_node = next_node

    def __repr__(self):
        return f"({self.val})->{self.next_node}"


class LinkedList:
    def __init__(self, iterable=None):
        self.head = None
        self._length = 0
        if type(iterable) in [list, tuple, str]:
            for item in iterable:
                self.push(item)
        elif iterable is not None:
            raise TypeError("An iterable must be provided.")

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
        pass

    def search(self, val):
        pass

    def remove(self, node):
        pass

    def display(self):
        return f"({self.head.val})->{self.head.next_node}"


# test = LinkedList()
# test.push(37)
# print(test)
# test.push(99)
# print(test)
# test.push(12)
# print(test)
#
# breakpoint()

# a = LinkedList()  # a = () --> None
# a.push(37)  # a = (37) --> None
# a.push(99)  # a = (99) --> (37) --> None
