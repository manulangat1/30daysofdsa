"""
You have 2 numbers represented by a linked list, where each node contains a single digit, the digits are stored in reverse order such that 1's digit is at the head of the list.
Write a function that adds two number and returns sum as a linked list 
"""

from common_class import LinkedList


def sumOfLists(llA, llB):
    n1 = llA.head
    n2 = llB.head

    carry = 0
    ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10))
        carry = result / 10
    print(ll)
    return ll


customLL = LinkedList()

a = customLL.generate(3, 1, 5)
b = customLL.generate(3, 5, 10)
print(a)
print(b)

sumOfLists(a, b)
