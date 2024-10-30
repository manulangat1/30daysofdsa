class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class CircularSingleLinkedList:
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

    def createSCLL(self, nodeValue):
        newNode = Node(nodeValue)
        if self.head is None:
            self.head = newNode
            self.head.next = newNode
            self.tail = newNode
            self.tail.next = self.head
            return "THE SCLL has been created."

    def insert(self, nodeValue, location):
        newNode = Node(nodeValue)
        if self.head is None:
            newNode.next = newNode
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.tail.next = newNode
                self.head = newNode
                return "Insertion success"
            elif location == -1:
                newNode.next = self.head
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                    # add a break if the tempNode is head to stop the count

                    if tempNode == self.head:
                        print("** out of bounds in this call")
                        return

                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def traversal(self):
        # loop through the entire CSLL and print out the contents

        node = self.head
        while node:
            print(node.value)
            node = node.next

            if node == self.head:
                break

    def search(self, searchValue):
        node = self.head
        while node:
            if node.value == searchValue:
                return f"Found {node.value}"
            node = node.next
            if node == self.head:
                break
        return "Node not found"

    def deletion(self, location):
        """
        1. When only one node in the list - set head and tail to node
        2. More than one node - traverse till that node and delete it
        3. last node set the prev node to tail and link it to the head.
        """
        if self.head is None:
            return "No CSLL for ops to continue"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head.next
                    self.head = tempNode
                    self.tail.next = tempNode

            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                node = self.head
                index = 0
                while index < location - 1:
                    node = node.next
                    index += 1
                node.next = node.next.next

    def deleteEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None


SCLL = CircularSingleLinkedList()
SCLL.createSCLL(7)
print([i.value for i in SCLL])
SCLL.insert(10, 0)
print([i.value for i in SCLL])
SCLL.insert(11, -1)
print([i.value for i in SCLL])

print(SCLL.insert(15, 1))
print([i.value for i in SCLL])

SCLL.traversal()

print(SCLL.search(11))
print("----->")
print([i.value for i in SCLL])
SCLL.deletion(0)
print("----->")
print([i.value for i in SCLL])

SCLL.deletion(1)
print("----->")
print([i.value for i in SCLL])

SCLL.deleteEntireCSLL()
print("----->")
print([i.value for i in SCLL])
