# time and space  complexity is O(1)  for all operations


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class QueueLinkedList:
    def __init__(self):
        self.LinkedList = LinkedList()

    # check whether
    def enque(self, value):
        newNode = Node(value)
        if self.LinkedList.head is None:
            self.LinkedList.head = newNode
            self.LinkedList.tail = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode

    def dequeu(self):
        tempNode = self.LinkedList.head
        if self.LinkedList.head == self.LinkedList.tail:
            self.head = None
            self.tail = None
        else:
            self.LinkedList.head = self.LinkedList.head.next
        return tempNode

    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None


myQueue = QueueLinkedList()
print([str(x) for x in myQueue.LinkedList])
for i in range(1, 5):
    myQueue.enque(i)
print([str(x) for x in myQueue.LinkedList])
for i in range(1, 6):
    myQueue.dequeu()
print([str(x) for x in myQueue.LinkedList])
