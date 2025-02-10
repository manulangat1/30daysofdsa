"""
    The tail points to the head as it's next reference
"""


class Node:
    def __init__(self, value=None):
        self.next = None
        self.value = value

    def __str__(self):
        return str(self.value)


class CSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    # time complexity is o(n) and space complexity is o(1)
    # can be at the start, any point or at the end of the CSLL.
    def insertion(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.tail.next = newNode
                self.head = newNode
            elif location == -1:
                """
                loop through and get the last item
                """
                # tempNode = self.head
                # while tempNode:
                #     if tempNode == self.tail:
                #         break
                #     tempNode = tempNode.next
                newNode.next = self.head
                self.tail.next = newNode
                self.tail = newNode
            else:
                """
                loop through the CSLL and get the location.
                """
                tempNode = self.head
                index = 0
                while index < location - 1:
                    index += 1
                    tempNode = tempNode.next
                nextNode = tempNode.next
                newNode.next = nextNode
                tempNode.next = newNode

                if tempNode == self.tail:
                    self.tail = newNode
                    newNode.next = self.head

    def traversal(self):
        if self.head is None:
            return
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next

    def search(self, item):
        if self.head is None:
            return
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == item:
                    return True
                if tempNode == self.tail:
                    return False
                tempNode = tempNode.next
            return False

    def deletion(self, location):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            if location == 0:
                if self.tail == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    nextNode = self.head.next
                    self.tail.next = nextNode
                    self.head = nextNode
            elif location == -1:
                tempNode = self.head
                while tempNode:
                    if tempNode.next == self.tail:
                        break
                    tempNode = tempNode.next
                tempNode.next = self.head
                self.tail = tempNode
            else:
                index = 0
                tempNode = self.head
                while index < location - 1:
                    if tempNode == self.tail:
                        break
                    index += 1
                    tempNode = tempNode.next
                print(tempNode)
                tempNode.next = tempNode.next.next

    def deleteEntireCSLL(self):
        self.head = None
        self.tail = None
        self.tail.next = None


newCSLL = CSinglyLinkedList()
print([i.value for i in newCSLL])
newCSLL.insertion(20, 0)
print([i.value for i in newCSLL])
newCSLL.insertion(30, 0)
print([i.value for i in newCSLL])
newCSLL.insertion(100, -1)
print([i.value for i in newCSLL])
newCSLL.insertion(1000, 1)
print([i.value for i in newCSLL])
# print(newCSLL.search(1))
# newCSLL.traversal()

newCSLL.deletion(-1)
print([i.value for i in newCSLL])
newCSLL.deletion(1)
print([i.value for i in newCSLL])
# newCSLL.deletion(1)
# print([i.value for i in newCSLL])
# newCSLL.deletion(0)
# print([i.value for i in newCSLL])
newCSLL.deleteEntireCSLL()
print([i.value for i in newCSLL])
