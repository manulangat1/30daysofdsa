class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node.next:
            yield node
            node = node.next
            # print(node.value)

    def print(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def traversal(self):
        if self.head is None:
            return "Empty SLL"
        else:
            node = self.head
            while node.next is not None:
                print(node.value)
                node = node.next

    def search(self, searchValue):
        if self.head is None:
            return "Empty SLL"
        else:
            node = self.head
            while node:
                if node.value == searchValue:
                    return f"Found {node.value}"
                else:
                    node = node.next
        return "Value does not exist"

    def insert(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            # self.head.next = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode

            elif location == -1:
                newNode.next = Node()
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                # newNode.next = tempNode.next.next
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

                if tempNode == self.tail:
                    self.tail = newNode


SLL = SLinkedList()
node1 = Node(1)
node2 = Node(2)
SLL.head = node1
SLL.head.next = node2
SLL.tail = node2


print([i.value for i in SLL])
SLL.print()
SLL.insert(8, 0)
print([i.value for i in SLL])
SLL.insert(10, 1)
print([i.value for i in SLL])
SLL.insert(100, 2)
print([i.value for i in SLL])
SLL.insert(100, 5)
print([i.value for i in SLL])

SLL.traversal()
print("--->")
print(SLL.search(1000))
