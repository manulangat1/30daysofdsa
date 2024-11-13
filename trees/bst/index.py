class BSTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None


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
    print(rootNode)
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)


def levelOrderTraversal(rootNode, level=0):
    if not rootNode:
        return
    customQ = []
    customQ.append(rootNode)
    while customQ:

        root = customQ.pop(0)
        data = root.data
        ret = " " * level + str(data)
        print(ret)
        # print(root.data)
        if root.leftChild:
            level -= 1
            customQ.append(root.leftChild)
        if root.rightChild:
            level += 3
            customQ.append(root.rightChild)


# time and space complexity if O(log N)
def insert(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    elif newNode.data <= rootNode.data:
        if not rootNode.leftChild:
            rootNode.leftChild = newNode
        else:
            insert(rootNode.leftChild, newNode)
    else:
        if not rootNode.rightChild:
            rootNode.rightChild = newNode
        else:
            insert(rootNode.rightChild, newNode)


def search(rootNode, searchValue):
    if not rootNode:
        return
    print(rootNode.data, searchValue)
    if rootNode.data == searchValue:
        return "Found"

    elif searchValue <= rootNode.data:
        # if rootNode.leftChild:
        if rootNode.leftChild.data == searchValue:
            return "Found"
        else:
            search(rootNode.leftChild, searchValue)
    else:
        # if rootNode.rightChild:
        if rootNode.rightChild.data == searchValue:
            return "Found"
        else:
            search(rootNode.rightChild, searchValue)

    return "Not found"


newBST = BSTreeNode(5)
leftChild = BSTreeNode(4)
rightChild = BSTreeNode(6)
newBST.leftChild = leftChild
newBST.rightChild = rightChild

levelOrderTraversal(newBST)
newNode = BSTreeNode(10)
newNode.rightChild = None
newNode.leftChild = None
insert(newBST, newNode)
levelOrderTraversal(newBST)
newNode2 = BSTreeNode(1)
insert(newBST, newNode2)
levelOrderTraversal(newBST)

# print(search(newBST, 99))
# print(search(newBST, 10))


def minValueNode(bstNode):
    current = bstNode
    while current.leftChild is not None:
        current = current.leftChild
    return current


def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return None
    if nodeValue <= rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            tempNode = rootNode.rightChild
            rootNode = None
            return tempNode
        if rootNode.rightChild is None:
            tempNode = rootNode.leftChild
            rootNode = None
            return tempNode

        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode


print(deleteNode(newBST, 4))
levelOrderTraversal(newBST)
