"""
 You have two numbers represented by a linked list, where each node contains a single digit.
   The digits are stored in reverse order, such that the 1's digit is at the head of the list.
   Write a function that adds the two numbers and returns the sum as a linked list.
"""

from LinkedList import LinkedList


def sumOfTwo(ll1, ll2):
    n1 = ll1.head
    n2 = ll2.head
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
    return ll


customLL1 = LinkedList()
customLL1.generate(3, 1, 5)
customLL2 = LinkedList()
customLL2.generate(3, 6, 9)
print(customLL1, "link ---> link", customLL2)
print(sumOfTwo(customLL1, customLL2))
