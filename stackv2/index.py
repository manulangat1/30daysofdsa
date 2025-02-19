""""
Pile of objects stacked vertically  e.g pile of dinner plates. 
LIFO method - last in first out method 
Common operations 
- Create 
- push 
- pop 
- peek 
- isEmpty 
- deleteStack
"""


class Stack:
    def __init__(self):
        self.stackList = []

    def __str__(self):
        values = self.stackList.reverse()
        values = [str(x) for x in self.stackList]
        return "-->".join(values)

    def push(self, value):
        self.stackList.append(value)

    def pop(self):
        return self.stackList.pop()

    def peek(self):
        return self.stackList[0]

    def isEmpty(self):
        return True if self.stackList == [] else False

    def deleteStack(self):
        self.stackList = []


myStackList = Stack()
for i in range(1, 5, 3):
    print(i)
    myStackList.push(i)
print(myStackList)
print(myStackList.peek())
