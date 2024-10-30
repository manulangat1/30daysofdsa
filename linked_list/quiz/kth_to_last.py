from common_class import LinkedList


def kth_to_last(ll, n):
    if not ll.head:
        return
    else:
        pointer1 = ll.head
        pointer2 = ll.head

        for i in range(n):
            if pointer2 is None:
                return None
            pointer2 = pointer2.next

        while pointer2:
            pointer2 = pointer2.next
            pointer1 = pointer1.next
        return pointer1


linked_list = LinkedList()
linked_list.generate(10, 0, 88)
print(linked_list)
print(kth_to_last(linked_list, 8))
