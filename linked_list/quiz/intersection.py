"""
Given two (singly) linked lists, determine if the two lists intersect.
Return the intersecting node. Note that the intersection is defined based on reference, not value.
That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.
"""

from LinkedList import LinkedList, Node


# def intersection(ll):
#     """
#     Approach is to have a fast and slow pointer, then check whether these 2 have the same ref.
#     """
#     fast = ll.head
#     slow = ll.head
#     while fast:
#         if fast.next is None:
#             return
#         if fast == slow:
#             return slow
#         fast = fast.next.next
#         slow = slow.next
#     return slow


def intersection(llA, llB):
    if llA.tail != llB.tail:
        return False
    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    return longerNode


def addSameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode


customLL = LinkedList()
customLL.generate(10, 20, 23)
customLL2 = LinkedList()
customLL2.generate(3, 6, 9)
addSameNode(customLL, customLL2, 10)
addSameNode(customLL, customLL2, 11)
addSameNode(customLL, customLL2, 12)
print(customLL, " another", customLL2)
print(intersection(customLL, customLL2))
