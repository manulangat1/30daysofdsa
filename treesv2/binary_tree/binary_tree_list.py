class BinaryTree:
    def __init__(self, size):
        """
        time complexity is O(1)
        space complexity is O(n)
        """
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        """
        time and space complexity is O(1)
        """
        if self.lastUsedIndex + 1 == self.maxSize:
            return
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "Done"

    def searchNode(self, searchValue):
        for i in range(len(self.customList)):
            if self.customList[i] == searchValue:
                return True
        return False

    def preOrder(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrder(index * 2)
        self.preOrder((index * 2) + 1)

    def inOrder(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrder(index * 2)
        print(self.customList[index])
        self.inOrder((index * 2) + 1)

    def postOrder(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrder(index * 2)
        self.postOrder((index * 2) + 1)
        print(self.customList[index])

    def levelOrder(self, index):
        for i in range(len(self.customList)):
            print(self.customList[i])

    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return
        for i in range(1, self.lastUsedIndex):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "Done"

    def deleteEntire(self):
        self.customList = None


newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
print(newBT.searchNode("cold"))
newBT.preOrder(1)
print("--->")
newBT.postOrder(1)
print("--->")
newBT.levelOrder(1)
