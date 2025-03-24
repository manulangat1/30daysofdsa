"""
    This  follows the FIFO method. 
    Queue operations. 
     - Create
     - Enqueue 
     - Deqeue 
     - Peek  
     - isEmpty 
     - isFull (not needed for linked list implementation)
     - deleteQueue. ( set the linked list implementation to None)
    Implementations:
    1. Python List 
        - Queue without capacity. 
        - Queue with capacity ( circular queue)
    2. Linked List

"""


class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return "<--->".join(values)

    def isEmpty(self):
        return True if self.items == [] else False

    # worst case is O(n)
    def enqueue(self, value):
        return self.items.append(value)

    # time complexity is O(n)
    def dequeue(self):
        if self.isEmpty():
            return
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def delete(self):
        self.items = None


myQueue = Queue()
print(myQueue)
for i in range(1, 5):
    myQueue.enqueue(i)
print(myQueue)
print("00000")
print(myQueue.peek())
# for i in range(4):
#     myQueue.dequeue()
# print(myQueue)
