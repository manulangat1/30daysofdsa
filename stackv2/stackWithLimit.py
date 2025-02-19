class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "<-->".join(values)

    def isEmpty(self):
        return True if self.list == [] else False

    def isFull(self):
        return True if len(self.list) == self.maxSize else False

    def push(self, value):
        if self.isFull():
            return "Full stack"
        return self.list.append(value)

    def pop(self):
        if self.isEmpty():
            return
        return self.list.pop()

    def delete(self):
        self.list = None


customStack = Stack(4)
for i in range(1, 6):
    print(customStack.push(i))
print("<--->")
print(customStack)
