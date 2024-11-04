"""
Design  a stack which in addition to push and pop has a function min which returns the minimum element? Push , pop and min should all operate in O(1)
since it requires O(1), we need to implement it using a linked list
"""


class Node:
    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        string = str(self.value)
        if self.next:
            string += "," + str(self.next)
        return string


# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None
#         self.tail = None


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.minNode = None

    def min(self):
        if not self.minNode:
            return None
        return self.minNode.value

    def push(self, item):
        if self.minNode and (self.minNode.value < item):
            self.minNode = Node(value=self.minNode.value, next=self.minNode)
        else:
            self.minNode = Node(value=item, next=self.minNode)
        self.top = Node(value=item, next=self.top)

    def pop(self):
        if not self.top:
            return None
        self.minNode = self.minNode.next
        item = self.top.value
        self.top = self.top.next
        return item


custStack = Stack()
# for _ in range(5):
#     custStack.push(_)
# for _ in range(3):
#     custStack.push(_)
custStack.push(5)
print(custStack.min())
custStack.push(6)
print(custStack.min())
custStack.push(-5)
print(custStack.min())
custStack.push(3)
print(custStack.min())
custStack.pop()
print(custStack.min())
