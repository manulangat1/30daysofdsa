class Stack:
    def __init__(self) -> None:
        self.list = []

    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    def isEmpty(self):
        """
        Time and space complecity is 0(1)
        """
        return True if len(self.list) == 0 else False

    def push(self, value):
        return self.list.append(value)

    def pop(self):
        if self.isEmpty():
            return
        return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return
        return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None


customStack = Stack()
print(customStack)
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.pop())
print(customStack.peek())
customStack.delete()
print("--->")
print(customStack)
