class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.head:
                break

    # creation of  circular doubly linked list

    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        newNode.next = newNode
        newNode.prev = newNode
        self.head = newNode
        self.tail = newNode

    def insertion(self, nodeValue, location):
        """
        1. At the start of the CDLL.
        2. At any point of the CDLL.
        3. At the end of the CDLL.
        """

        newNode = Node(nodeValue)
        if self.head is None:
            newNode.next = newNode
            newNode.prev = newNode
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0

                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                    if tempNode == self.head:
                        break
                print(index, tempNode.value)
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    def traversal(self):
        tempNode = self.head
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.next
            if tempNode == self.head:
                break

    def reverse_traversal(self):
        tempNode = self.tail
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.prev
            if tempNode == self.tail:
                break

    def search(self, searchValue):
        tempNode = self.head
        while tempNode:
            if tempNode.value == searchValue:
                return "Found"
            tempNode = tempNode.next
            if tempNode == self.head:
                break
        return "Not found"

    def deletion(self, location):
        if not self.head:
            return "Empty list"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                    return "removed success"
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                    return "removed success"
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                currNode = self.head
                index = 0
                while index < location - 1:
                    currNode = currNode.next
                    index += 1
                currNode.next = currNode.next.next
                currNode.next.prev = currNode

    def deleteCDLL(self):
        if not self.head:
            print("Empty CDLL")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None

            print("Success")


CDLL = CircularDoublyLinkedList()
CDLL.createCDLL(20)
print([i.value for i in CDLL])
CDLL.insertion(10, 0)
print([i.value for i in CDLL])
# CDLL.insertion(30, -1)
# print([i.value for i in CDLL])
# CDLL.insertion(35, 1)
# print([i.value for i in CDLL])
# print(CDLL.deletion(0))
# print([i.value for i in CDLL])
# print(CDLL.deletion(1))
# print([i.value for i in CDLL])
CDLL.deleteCDLL()
print([i.value for i in CDLL])
