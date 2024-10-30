class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def createDLL(self, value):
        newNode = Node(value)
        newNode.next = newNode
        self.head = newNode

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            # if node.next == self.head:
            #     break

    def insertion(self, nodeValue, location):
        """
        1. At the start of DLL. - Check whether
        2. middle of the DLL
        3. end of the DLL
        """
        newNode = Node(nodeValue)
        if self.head is None:
            return
            # newNode.next = newNode
            # self.head = newNode
            # self.tail = newNode
            # self.tail.prev = newNode
        else:
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
                return "Success"
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                node = self.head
                index = 0
                while index < location - 1:
                    node = node.next
                    index += 1
                print(node.value, "--->")
                newNode.next = node.next
                newNode.prev = node
                newNode.next.prev = newNode
                node.next = newNode

    def traversal(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def reverseTraversal(self):
        node = self.tail
        while node:
            print(node.value)
            node = node.prev

    def deletion(self):
        """
        1. Node is the only one in the list
        2. Deleting any given node.
        3. Deleting the last node.
        """


dLL = DoublyLinkedList()
newNode = Node(10)
dLL.head = newNode
dLL.tail = newNode
# dLL.createDLL(10)
# dLL.insertion(10, 0)
print([i.value for i in dLL])
dLL.insertion(11, 0)
print([i.value for i in dLL])
dLL.insertion(13, -1)
print([i.value for i in dLL])
dLL.insertion(14, 2)
print([i.value for i in dLL])
print("---> traversal")
dLL.traversal()

print("---> reverse traversal")
dLL.reverseTraversal()
