class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        # self.tail = None

    def __str__(self) -> str:
        return str(value)


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # def enqueu(self, value):


class Queue:
    def __init__(self) -> None:
        self.linkedList = LinkedList()

    def __str__(self) -> str:
        values = [str(x.value) for x in self.linkedList]
        return "->".join(values)

    def enque(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    def isEmpty(self):
        return True if self.linkedList.head is None else False

    def dequeu(self):
        if self.isEmpty():
            return
        tempNode = self.linkedList.head
        if self.linkedList.head == self.linkedList.tail:
            self.linkedList.head = None
            self.linkedList.tail = None
        else:
            self.linkedList.head = self.linkedList.head.next
        return tempNode

    def peek(self):
        if self.isEmpty():
            return
        return self.linkedList.head

    def delete(self):
        if self.isEmpty():
            return
        self.linkedList.head = None
        self.linkedList.tail = None


custQueue = Queue()
print(custQueue)
print(custQueue.isEmpty())
for i in range(5):
    custQueue.enque(i)
print(custQueue)
print(custQueue.isEmpty())
for _ in range(3):

    custQueue.dequeu()
print(custQueue)
custQueue.delete()
print(custQueue)
