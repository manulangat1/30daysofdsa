class AVLNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


newAVL = AVLNode(10)


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


def searchNode(rootNode, searchNode):
    if not rootNode:
        return "not found"
    if rootNode.data == searchNode:
        return "Found"
    elif rootNode.data <= rootNode.data:
        if rootNode.leftChild.data is not None == searchNode:
            return "Found"
        else:
            searchNode(rootNode.leftChild, searchNode)
    else:
        if rootNode.rightChild.data is not None == searchNode:
            return "Found"
        else:
            searchNode(rootNode.rightChild, searchNode)
    return "Not found"


print(searchNode(newAVL, 100))


"""
Rotation 
    Rotation is required. 
    Rotation is not required - same as the BST
"""
