"""
Describe how you can use one python list to create 3 queues
"""


class MultiStack:
    def __init__(self, stackSize) -> None:
        self.numberStacks = 3
        self.custList = [0] * (stackSize * self.numberStacks)
        self.sizes = [0] * self.numberStacks
        self.stackSize = stackSize

    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.stackSize:
            return True
        return False

    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        return False

    def indexOfTop(self, stacknum):
        offset = stacknum * self.stackSize
        return offset + self.sizes[stacknum] - 1

    def push(self, item, stacknum):
        if self.isFull(stacknum):
            return
        else:
            self.sizes[stacknum] += 1
            self.custList[self.indexOfTop(stacknum)] = item

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            self.sizes[stacknum] -= 1
            self.custList[self.indexOfTop(stacknum)] = 0
            return value

    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return
        else:
            return self.custList[self.indexOfTop(stacknum)]


customStack = MultiStack(6)
print(customStack.isEmpty(0))
print(customStack.isFull(1))
customStack.push(1, 1)
customStack.push(2, 0)
customStack.push(3, 2)
print(customStack.peek(1))
