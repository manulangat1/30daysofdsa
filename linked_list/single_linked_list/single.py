class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # adding a node at the start, mid and end of a linked list
    def insertion(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                self.tail.next = newNode
                self.tail = newNode
            else:
                count = 0
                tempNode = self.head
                while count < location - 1 and tempNode:
                    count += 1
                    tempNode = tempNode.next
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

                if tempNode == self.tail:
                    self.tail = newNode

    # time complexity is o(n)
    def traversal(self):
        if self.head is None:
            return
        else:
            node = self.head
            while node:
                print(node)
                node = node.next

    # time complexity is o(n)
    def search(self, item):
        if self.head is None:
            return
        else:
            node = self.head
            while node:
                if node.value == item:
                    return "Found at item"
                node = node.next
        return False

    # delete from start, any point or at the end.
    def deletion(self, location):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            if location == 0:

                self.head = self.head.next
            elif location == -1:
                # loop through all the items and find the next to the tail
                tempNode = self.head
                while tempNode:
                    if tempNode.next == self.tail:
                        break
                    tempNode = tempNode.next
                tempNode.next = None
                self.tail = tempNode
            else:
                index = 0
                tempNode = self.head
                while index < location - 1:
                    index += 1
                    tempNode = tempNode.next
                tempNode.next = tempNode.next.next

    def deleteEntireSLL(self):
        self.head = None
        self.tail = None


# node = Node(10)
# node2 = Node(11)
# newSLL = SLinkedList()
# newSLL.head = node
# node.next = node2
# newSLL.tail = node2

newSLL = SLinkedList()
newSLL.insertion(10, 0)
print([i.value for i in newSLL])
newSLL.insertion(100, -1)
print([i.value for i in newSLL])
newSLL.insertion(20, 0)
print([i.value for i in newSLL])
newSLL.insertion(30, -1)
print([i.value for i in newSLL])
newSLL.insertion(35, 3)
print([i.value for i in newSLL])
newSLL.insertion(70, 5)
print([i.value for i in newSLL])
newSLL.insertion(1000, -1)
print(len([i.value for i in newSLL]))

# newSLL.traversal()
print(newSLL.search(100))
print("*******")
print([i.value for i in newSLL])
newSLL.deletion(0)
print([i.value for i in newSLL])
print("*******")
print([i.value for i in newSLL])
newSLL.deletion(-1)
print([i.value for i in newSLL])
newSLL.deletion(2)
print([i.value for i in newSLL])
newSLL.deleteEntireSLL()
print([i.value for i in newSLL])
