class Queue:
    def __init__(self, maxSize) -> None:
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.top = -1
        self.start = -1

    def __str__(self) -> str:
        return " ".join([str(x) for x in self.items])

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            return
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0

            self.items[self.top] = value
            return "Element inserted successfully"


customQueue = Queue(3)
print(customQueue.isFull())
for _ in range(3, -1, -1):
    customQueue.enqueue(_)
print(customQueue)
