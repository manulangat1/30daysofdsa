from LinkedList import LinkedList

"""
use a set for this, 
1. Check whether the item is in the set, if yes remove it 
2. if no append it to the set. 
"""


def removeDuplicates(head):
    node = head.head
    visited = set([node.value])
    while node.next:
        if node.next.value in visited:
            node.next = node.next.next
        else:
            visited.add(node.value)
            node = node.next
    return head


customLL = LinkedList()
customLL.generate(10, 20, 23)
print(customLL)
print(removeDuplicates(customLL))
