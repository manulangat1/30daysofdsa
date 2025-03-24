class PlateStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return str(self.stacks)

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

    def popAt(self, stackNum):
        if len(self.stacks[stackNum]) > 0:
            return self.stacks[stackNum].pop()
        return None


customStack = PlateStack(2)
for i in range(1, 7):
    customStack.push(i)
print(customStack)
customStack.popAt(2)
print(customStack)
