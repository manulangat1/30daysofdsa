class AVLNode:

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.leftChild)
    preOrder(rootNode.rightChild)


def inOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.leftChild)
    print(rootNode.data)
    inOrder(rootNode.rightChild)


def postOrder(rootNode):
    if not rootNode:
        return
    postOrder(rootNode.leftChild)
    postOrder(rootNode.rightChild)
    print(rootNode.data)


def levelOrder(rootNode):
    if not rootNode:
        return

    customQ = []
    customQ.append(rootNode)

    while customQ:
        root = customQ.pop()
        print(root.data)
        if root.leftChild is not None:
            customQ.append(root.leftChild)
        if root.rightChild is not None:
            customQ.append(root.rightChild)


def searchNode(rootNode, nodeValue):
    # if not rootNode:
    #     return
    if rootNode.data == nodeValue:
        return True
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            return True
        else:
            searchNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        if rootNode.rightChild.data == nodeValue:
            return True
        else:
            searchNode(rootNode.rightChild, nodeValue)


def getHeight(rootNode):
    if not rootNode:
        return
    return rootNode.height


def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftchild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(
        getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild)
    )

    newRoot.height = 1 + max(
        getHeight(newRoot.leftChild), getHeight(newRoot.rightChild)
    )
    print(newRoot)
    return newRoot


def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + (
        max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    )
    newRoot.height = 1 + (
        max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    )
    return newRoot


def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)


def insertion(rootNode, nodeValue):
    """
    case 1. Rotation is not required.
    case 2. Rotation is required.
            2.1 Left left condition.
            2.2 Left right condition.
            2.3 right right condition.
            2.4 right left condition.
    """
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertion(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertion(rootNode.rightChild, nodeValue)
    rootNode.height = 1 + (
        max(getHeight(rootNode.rightChild), getHeight(rootNode.leftChild))
    )
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)


newAVL = AVLNode(5)
# left = AVLNode(20)
# right = AVLNode(30)

# newAVL.leftChild = left
# newAVL.rightChild = right
insertion(newAVL, 10)


preOrder(newAVL)
print("---> in order")
inOrder(newAVL)
print("---> post order")
postOrder(newAVL)
print("---> level order")
levelOrder(newAVL)
print("---> search")
# print(searchNode(newAVL, 20))
print(newAVL.leftChild.data)
print(newAVL.rightChild.data)
