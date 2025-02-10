"""
Each node has prev and next references except the head and tail
"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class DoublyLinkedList:
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

    def insert(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.tail.next = newNode
        else:
            if location == 0:
                self.tail.next = self.head
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.prev = self.tail
                self.tail.next = newNode
                newNode.next = self.head
                self.tail = newNode
            else:
                """
                1. loop till you get the node at the said location

                """
                index = 0
                tempNode = self.head
                while index < location - 1:

                    tempNode = tempNode.next
                    index += 1
                print(location, tempNode, tempNode.next, index)
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

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

    def reverseTraversal(self):
        if self.head is None:
            return
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    def search(self, item):
        if self.head is None:
            return
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == item:
                    return True
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next
            return False

    """
     We also have 3 cases ie start, any point or at the end. 
    """

    def deletion(self, location):
        if self.head is None:
            return None
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    nextNode = self.head.next
                    self.tail.next = nextNode
                    self.head = nextNode
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
            else:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    index = 0
                    tempNode = self.head
                    while index < location - 1:
                        index += 1
                        tempNode = tempNode.next
                    tempNode.next = tempNode.next.next
                    tempNode.next.prev = tempNode

    def deleteEntireDLL(self):
        if self.head is None:
            return
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None


newDLL = DoublyLinkedList()
newDLL.insert(100, 0)
print([i.value for i in newDLL])
for i in range(3):
    newDLL.insert((200 + i), -1)
print([i.value for i in newDLL])
newDLL.insert(500, 3)
print([i.value for i in newDLL])
newDLL.reverseTraversal()
print(newDLL.search(450))
print(newDLL.search(100))
print([i.value for i in newDLL])
newDLL.deletion(0)
print([i.value for i in newDLL])
print([i.value for i in newDLL])
newDLL.deletion(-1)
print([i.value for i in newDLL])
# for k in range(4):
#     print(k)
#     newDLL.deletion(k)
# newDLL.deletion(0)
# print([i.value for i in newDLL])
print("now running!")
newDLL.deleteEntireDLL()
print([i.value for i in newDLL])
