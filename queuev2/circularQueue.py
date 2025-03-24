class CircularQueue:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.items = [None] * self.maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return "<--->".join(values)

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        if self.start == 0 and self.top + 1 == self.maxSize:
            return True
        return False

    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def enqeue(self, value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "Done"
