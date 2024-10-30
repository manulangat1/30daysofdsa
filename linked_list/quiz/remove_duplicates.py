"""
Remove duplicates from an unsorted linked list
"""

from common_class import LinkedList


# def remove_duplicates(ll):
#     if not ll.head:
#         return
#     currNode = ll.head
#     tempSet = set([currNode.value])
#     while currNode.next:
#         if currNode.next.value in tempSet:
#             currNode.next = currNode.next.next
#         else:
#             tempSet.add(currNode.next.value)
#             currNode = currNode.next
#     return "Done"


def remove_duplicates(ll):
    if not ll.head:
        return
    currNode = ll.head
    while currNode:
        runner = currNode
        while runner.next:
            if runner.next.value == currNode.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        currNode = currNode.next
    return ll.head


customLL = LinkedList()
customLL.generate(10, 97, 99)
print(customLL)
remove_duplicates(customLL)
print(customLL)
