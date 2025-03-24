class TreeNode:
    def __init__(self, data):
        """
        Time and space complexity is O(1)
        """
        self.data = data
        self.leftChild = None
        self.rightChild = None


def preOrderTraversal(rootNode):
    """
    time complexity is O(n)
    space compelexity is O(n) due to use of stack compelexity
    """
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    customQ = []
    customQ.append(rootNode)
    while customQ:
        root = customQ.pop()
        print(root.data)
        if root.leftChild:
            customQ.append(root.leftChild)
        if root.rightChild:
            customQ.append(root.rightChild)


def searchNode(rootNode, search):
    if not rootNode:
        return
    customQ = []
    customQ.append(rootNode)
    while customQ:
        root = customQ.pop()

        if str(root.data).lower() == search.lower():
            return "Found"
        if root.leftChild:
            customQ.append(root.leftChild)
        if root.rightChild:
            customQ.append(root.rightChild)


def insertNode(rootNode, newNode):
    if not rootNode:
        return
    customQ = []
    customQ.append(rootNode)
    while customQ:
        root = customQ.pop()
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


def getDeepestNode(rootNode):
    if not rootNode:
        return
    customQ = []
    customQ.append(rootNode)
    while customQ:
        root = customQ.pop()
        if root.leftChild:
            customQ.append(root.leftChild)
        if root.rightChild:
            customQ.append(root.rightChild)
    deepestNode = root
    return deepestNode


def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    customQ = []
    customQ.append(rootNode)
    while customQ:
        root = customQ.pop()
        if root == dNode:
            root = None
            return
        if root.rightChild:
            if root.rightChild == dNode:
                root.rightChild = None
            else:
                customQ.append(root.rightChild)
        if root.leftChild:
            if root.leftChild == dNode:
                root.leftChild = None
            else:
                customQ.append(root.leftChild)


def deleteNodeBT(rootNode, node):
    if not rootNode:
        return
    customQ = []
    customQ.append(rootNode)
    while customQ:
        root = customQ.pop()
        if root.data == node:
            dNode = getDeepestNode(root)
            root.data = dNode.data
            deleteDeepestNode(rootNode, dNode)
            return "Delete success"
        if root.leftChild:
            customQ.append(root.leftChild)
        if root.rightChild:
            customQ.append(root.rightChild)


newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("COld")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

preOrderTraversal(newBT)
print("--->")
inOrderTraversal(newBT)
print("--->")
postOrderTraversal(newBT)
print("--->")
levelOrderTraversal(newBT)
print("--->, Search")
print(searchNode(newBT, "Drinks"))
newNode = TreeNode("Cola")
newNode1 = TreeNode("Fanta")
newNode2 = TreeNode("Tea")
newNode3 = TreeNode("Coffee")
insertNode(newBT, newNode)
insertNode(newBT, newNode1)
insertNode(newBT, newNode2)
insertNode(newBT, newNode3)
levelOrderTraversal(newBT)
print("---->")
deepestNode = getDeepestNode(newBT)
print(deepestNode.data)
deleteDeepestNode(newBT, deepestNode)

print("---->")
levelOrderTraversal(newBT)

deleteNodeBT(newBT, "Fanta")
print("---->")
levelOrderTraversal(newBT)
deleteNodeBT(newBT, "Tea")
print("---->")
levelOrderTraversal(newBT)
