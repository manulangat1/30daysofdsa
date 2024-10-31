class StackList:
    def __init__(self, maxSize) -> None:
        self.maxSize = maxSize
        self.list = []

    def __str__(self) -> str:
        if self.isEmpty() or self.list is None:
            return "Empty stack"
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    def isEmpty(self):
        return True if self.list == [] else False

    def isFull(self):
        return True if len(self.list) == self.maxSize else False

    def push(self, value):
        if self.isFull():
            return
        return self.list.append(value)

    def peek(self):
        if self.isEmpty():
            return
        return self.list[len(self.list) - 1]

    def pop(self):
        if self.isEmpty():
            return
        return self.list.pop()

    def delete(self):
        self.list = None
        self.maxSize = None


customStack = StackList(5)
print(customStack)
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.pop())
print(customStack.peek())
customStack.delete()
print("--->")
print(customStack)
