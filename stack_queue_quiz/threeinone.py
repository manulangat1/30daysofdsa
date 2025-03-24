"""
Use a single python list to implement 3 stacks. 
"""


class MultiStack:
    def __init__(self, stackSize):
        self.numberStacks = 3
        self.customList = [0] * (stackSize * self.numberStacks)
        self.sizes = [0] * self.numberStacks
        self.stackSize = stackSize

    def isFull(self, stacknum):
        return True if self.sizes[stacknum] == self.stackSize else False

    def isEmpty(self, stacknum):
        return True if self.sizes[stacknum] == 0 else False

    def indexOfTop(self, stacknum):
        offset = stacknum * self.stackSize
        return offset + self.sizes[stacknum] - 1

    def push(self, value, stacknum):
        if self.isFull(stacknum):
            return
        self.sizes[stacknum] += 1
        self.customList[self.indexOfTop(stacknum)] = value

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return
        self.sizes[stacknum] -= 1
        self.customList[self.indexOfTop(stacknum)] = 0

    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return
        return self.customList[self.indexOfTop(stacknum)]


myMultiStack = MultiStack(5)
print(myMultiStack.isFull(1))
print(myMultiStack.isFull(2))
print(myMultiStack.isEmpty(1))
print(myMultiStack.isEmpty(2))
