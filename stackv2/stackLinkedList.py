# from .. import linked_list

# linked_list.quiz.LinkedList import LinkedList
"""
time and space complexity of all these operations is O(1)
"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class StackList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def push(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def isEmpty(self):
        return True if self.head is None else False

    def delete(self):
        self.head = None


myLLStack = StackList()

myLLStack.push(5)
myLLStack.push(6)
myLLStack.push(7)
print([str(x.value) for x in myLLStack])
for _ in range(1, 4):
    myLLStack.pop()
print("<--->")
print([str(x.value) for x in myLLStack])
