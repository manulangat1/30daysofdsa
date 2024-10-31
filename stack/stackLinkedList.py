"""
Time and space complexity for all operations in this case is 0(1)
"""


class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None


class Stack:
    def __init__(self) -> None:
        self.LinkedList = LinkedList()

    def isEmpty(self):
        return True if self.LinkedList.head is None else False

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.LinkedList.head
        self.LinkedList.head = newNode

    def peek(self):
        peekValue = self.LinkedList.head.value
        return peekValue

    def pop(self):
        peekValue = self.LinkedList.head.value
        self.LinkedList.head = self.LinkedList.head.next
        return peekValue

    def __iter__(self):
        node = self.LinkedList.head
        while node:
            yield node
            node = node.next

    def delete(self):
        self.LinkedList.head = None


customStack = Stack()
print(customStack.isEmpty())
print([i.value for i in customStack])
for _ in range(10, -1, -2):
    customStack.push(_)
print([i.value for i in customStack])
print(customStack.peek())
print(customStack.pop())
print([i.value for i in customStack])
print(customStack.peek())
