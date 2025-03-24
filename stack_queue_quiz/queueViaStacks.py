"""
Implement Queue class with 2 stacks
"""


class Stack:
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def push(self, item):
        return self.list.append(item)

    def pop(self):
        return None if len(self.list) == 0 else self.list.pop()


class QueueViaStack:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueue(self, item):
        self.inStack.push(item)

    def dequeue(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop()
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return result


customQ = QueueViaStack()
for i in range(1, 4):
    customQ.enqueue(1)
print(customQ.dequeue())
print(customQ.dequeue())
