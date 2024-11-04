class PlateStack:

    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.stacks = []

    def __str__(self) -> str:
        return self.stacks

    def push(self, item):
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()

    def pop_at(self, stackNumber):
        if len(self.stacks[stackNumber]) > 0:
            return self.stacks[stackNumber].pop()
        return None


customStack = PlateStack(2)
customStack.push(1)
customStack.push(2)
customStack.push(3)
# print(customStack)
print(customStack.pop())
print(customStack.pop_at(1))
