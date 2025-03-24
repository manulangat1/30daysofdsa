"""
Design a stack in which in addition to push and pop has a fn minimum which returns the min element. 
Push, pop and min should all operate in o(1)

Since the constraint given is that it should operate in O(1), we should use a LL
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        string = str(self.value)
        # if self.next:
        #     string += "," + str(self.next)

        return string


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.minNode = None


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __iter__(self):
        node = self.LinkedList.head
        while node:
            yield node
            node = node.next

    def min(self):
        if not self.LinkedList.minNode:
            return None
        return self.LinkedList.minNode.value

    def push(self, value):
        if self.LinkedList.minNode and (self.LinkedList.minNode.value < value):
            self.LinkedList.minNode = Node(
                value=self.LinkedList.minNode.value, next=self.LinkedList.minNode
            )
        else:
            self.LinkedList.minNode = Node(value=value, next=self.LinkedList.head)
        self.LinkedList.head = Node(value, next=self.LinkedList.head)

    def pop(self):
        if not self.LinkedList.head:
            return None
        self.LinkedList.minNode = self.LinkedList.minNode.next
        item = self.LinkedList.head
        self.LinkedList.head = self.LinkedList.head.next
        return item


myStack = Stack()
print([str(i) for i in myStack])
# for i in range(1, 5):
myStack.push(10)
myStack.push(20)
myStack.push(3)
myStack.push(100)
# pass
print([str(i) for i in myStack])
print(myStack.min())
print(myStack.pop())
print(myStack.pop())
print(myStack.min())
