class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


# class BinarySearchTree:
#     def __init__(self):


newBST = TreeNode(None)


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    inOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


def insertion(rootNode, nodeValue):
    """
    There are 2 circumstances that one needs to check
        1. Root node is blank.
        2. Root node is not blank.
    Time and space complexity is O log n
    """
    if rootNode.data is None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = TreeNode(nodeValue)
        else:
            insertion(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = TreeNode(nodeValue)
        else:
            insertion(rootNode.rightChild, nodeValue)
    return "Node successfully inserted"


def levelOrder(rootNode):
    """
    time complexity is O(n)
    space complexity is O(n)
    This uses a queue instead of a stack.
    """
    if not rootNode:
        return
    customStack = []
    customStack.append(rootNode)

    # print([i.data for i in customStack])
    while customStack:
        root = customStack.pop()
        print(root.data)
        if root.leftChild:
            customStack.append(root.leftChild)
        if root.rightChild:
            customStack.append(root.rightChild)


def search(rootNode, searchItem):
    """
    time and space complexity isO logN
    """
    if rootNode.data == searchItem:
        return True
    elif searchItem < rootNode.data:
        if rootNode.leftChild.data == searchItem:
            print("Here")
            return True
        else:
            search(rootNode.leftChild, searchItem)
    else:
        if rootNode.rightChild.data == searchItem:
            print("here right")
            print("The nod is found")

        else:
            search(rootNode.rightChild, searchItem)


def minValueNode(bstNode):
    current = bstNode
    while current.leftChild is not None:
        current = current.leftChild
    return current


def deleteNode(rootNode, nodeValue):
    """
    time and space complexity is O log N
    """
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode.leftChild = None
            return temp
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode


def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None


insertion(newBST, 70)
insertion(newBST, 80)
insertion(newBST, 90)

preOrderTraversal(newBST)
print("---> in order")
inOrderTraversal(newBST)
print("---> post order")
postOrderTraversal(newBST)
print("Level order traversal")
levelOrder(newBST)
print("Search is ====>")
print(search(newBST, 90))
print(deleteNode(newBST, 90))
print("Level order traversal")
levelOrder(newBST)

deleteBST(newBST)
levelOrder(newBST)
