"""
    - Are the data structures in which each node has at most 2 children, often reffered to as left and right children
    - Family of data structures. 
    - Types of Binaty trees 
        1. Full binary tree - each node has 0 or 2 children. 
        2. Perfect binary tree - all leaf nodes are located at same place and are filled. 
        3. Complete binary tree - all levels are completly filled except the last one. 
        4. Balanced binary tree - all leaf are located from root at the same distance. 
        5. 
    - Representation 
        1. Linked List.
        2. Python List ( array)

"""


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def __str__(self) -> str:
        return str(self.data)


newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild


# time and space complexity is O(n)
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode)
    inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode)


# time and space complecity is O(n)
def levelOrderTraversal(rootNode):
    if not rootNode:
        return "Empty"
    customQ = []
    customQ.append(rootNode)
    while customQ:
        root = customQ.pop(0)
        print(root)
        if root.leftChild:
            customQ.append(root.leftChild)
        if root.rightChild:
            customQ.append(root.rightChild)


def searchNode(rootNode, searchValue):
    if not rootNode:
        return "Empty"
    customQ = []
    customQ.append(rootNode)
    while customQ:
        root = customQ.pop(0)
        print(root, searchValue)
        if str(root).lower() == str(searchValue).lower():
            return "Found"
        if root.leftChild:
            customQ.append(root.leftChild)
        if root.rightChild:
            customQ.append(root.rightChild)
    return "Not found"


def insert(rootNode, newNode):
    """
    - Root node is blank
    - tree exists and have to find a first vacant place.
    """
    if not rootNode:
        rootNode = newNode
    else:
        customQ = []
        customQ.append(rootNode)
        while customQ:
            root = customQ.pop(0)
            if root.leftChild:
                customQ.append(root.leftChild)
            else:
                root.leftChild = newNode
                return "Success"
            if root.rightChild:
                customQ.append(root.rightChild)
            else:
                root.rightChild = newNode
                return "Success"


print(preOrderTraversal(newBT))
print("level order traversal")
print(levelOrderTraversal(newBT))


print(searchNode(newBT, "Tea"))
print(searchNode(newBT, "Cold"))
newNode = TreeNode("Cola")
print(insert(newBT, newNode))


print("level order traversal")
print(levelOrderTraversal(newBT))


def getDeepestNode(rootNode):
    if not rootNode:
        return
    customQ = []
    customQ.append(rootNode)
    while customQ:
        root = customQ.pop(0)
        if root.leftChild:
            customQ.append(root.leftChild)
        if root.rightChild:
            customQ.append(root.rightChild)
    deepestNode = root.data
    return deepestNode


print(getDeepestNode(newBT), "deeepest node")


def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return

    customQ = []
    customQ.append(rootNode)
    while customQ:
        root = customQ.pop()

        if root.data is dNode:
            root.data = None
            return
        if root.rightChild:
            if root.rightChild.data is dNode:
                root.rightChild.data = None
                return
            else:
                customQ.append(root.rightChild)
        if root.leftChild:
            if root.leftChild.data is dNode:
                root.leftChild.data = None
                return
            else:
                customQ.append(root.leftChild)


newNode = getDeepestNode(newBT)
deleteDeepestNode(newBT, newBT)
levelOrderTraversal(newBT)
