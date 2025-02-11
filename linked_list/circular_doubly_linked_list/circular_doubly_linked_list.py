class Node:
    def __init__(self, value=None):
        self.next = None
        self.prev = None
        self.value = value

    def __str__(self):
        return str(self.value)


class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node == self.tail:
                break
            node = node.next

    # at the start , any point or at the end of the LL.
    def insertion(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.head.next = newNode
            self.tail = newNode
        else:
            if location == 0:
                if self.head is None:
                    self.head = newNode
                    self.head.next = newNode
                    self.tail = newNode
                else:
                    newNode.next = self.head
                    newNode.prev = self.tail
                    self.tail.next = newNode
                    self.head = newNode
            elif location == -1:
                newNode.prev = self.tail
                newNode.next = self.head
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    index += 1
                    tempNode = tempNode.next
                    if tempNode == self.tail:
                        break
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    def deletion(self, location):
        if self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.tail.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.head.prev = self.tail
                    self.tail.next = self.head
            else:
                index = 0
                tempNode = self.head
                while index < location - 1:
                    index += 1
                    tempNode = tempNode.next
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode


newCDLL = CDLL()
print([i.value for i in newCDLL])
newCDLL.insertion(80, 0)
print([i.value for i in newCDLL])
newCDLL.insertion(70, 0)
print([i.value for i in newCDLL])
newCDLL.insertion(90, -1)
print([i.value for i in newCDLL])
newCDLL.insertion(900, 1)
print([i.value for i in newCDLL])

newCDLL.deletion(-1)
print([i.value for i in newCDLL])
newCDLL.deletion(1)
print([i.value for i in newCDLL])
