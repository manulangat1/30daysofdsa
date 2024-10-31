"""
Given two singly LL, determine if the two lists intersect. Return the intersecting node. 
Note that the intersection is determined by reference not value. 
That is if the kth node of the 1st linked list is the exact same node ( by reference )
as the jth node of the second LL , then they are intersecting
"""

from common_class import LinkedList, Node


def intersection(llA, llB):
    """
    Algorithm
    1. check whether the tails are the same else return false

    time complexity is O(A+B)
    """

    if llA.tail is not llB.tail:
        return False
    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llA if lenA > lenB else llB

    diff = len(longer) - len(shorter)

    longerNode = longer.head
    shorterNode = shorter.head

    for _ in range(diff):
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


llA = LinkedList()

llA.generate(3, 1, 5)
# print(llA)

llB = LinkedList()

llB.generate(4, 5, 15)
# print(llB)

addSameNode(llA, llB, 80)
addSameNode(llA, llB, 90)
addSameNode(llA, llB, 60)

print(llA)
print(llB)

print(intersection(llA, llB))
