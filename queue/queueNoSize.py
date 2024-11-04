class Queue:
    def __init__(self) -> None:
        self.items = []

    def __str__(self) -> str:
        if self.isEmpty() or self.items is None:
            return "Empty"
        values = [str(x) for x in self.items]
        return "\n".join(values)

    def isEmpty(self):
        return True if self.items == [] else False

    def enque(self, value):
        return self.items.append(value)

    def peek(self):
        if self.isEmpty():
            return
        return self.items[0]

    def deque(self):
        if self.isEmpty():
            return
        return self.items.pop(0)

    def delete(self):
        self.items = None


customQueue = Queue()
print(customQueue)
for _ in range(10, -1, -3):
    customQueue.enque(_)
print(customQueue)
print(customQueue.peek())
print(customQueue.deque())
print("-->")
print(customQueue)
print("-->")
print(customQueue.delete())
print("-->")
print(customQueue)
print("-->")
