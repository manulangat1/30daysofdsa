"""
Partition a linked list in such a way that all the values less than x comes before x 
"""

from common_class import LinkedList


def partition(ll, x):
    currNode = ll.head
    ll.tail = ll.head

    while currNode:
        nextNode = currNode.next
        currNode.next = None
        if currNode.value < x:
            # assign it to the head
            currNode.next = ll.head
            ll.head = currNode
        else:
            ll.tail.next = currNode
            ll.tail = currNode
        currNode = nextNode

    if ll.tail.next is not None:
        ll.tail.next = None


customLL = LinkedList()

customLL.generate(10, 0, 88)
print(customLL)

partition(customLL, 70)
print(customLL)
