from LinkedList import LinkedList


def nthToLast(ll, n):
    if ll is None:
        return
    node = ll.head
    for i in range(n):
        if node is None:
            return
        node = node.next
    slow = ll.head
    while node:
        node = node.next
        slow = slow.next
    return slow


customLL = LinkedList()
customLL.generate(10, 20, 23)
print(customLL)
print(nthToLast(customLL, 5))
