"""
- DS in which the node has at most 2 children. left and right
- Family of DS.
Types.
    1. Full
    2. Perfect - all none leaf have 2 children and are at the same level.
    3. Complete  - all levels are completely filled except the last one
"""


class TreeNode:
    def __init__(self, data):
        """
        time and space complexity is O(1)
        """
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        return str(self.data)


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
        return
    customQ = []
    customQ.append(rootNode)

    while customQ:
        root = customQ.pop()
        print(root)
        if root.leftChild:
            customQ.append(root.leftChild)
        if root.rightChild:
            customQ.append(root.rightChild)


def search(rootNode, searchItem):
    """time complexity is O(n)"""
    if not rootNode:
        return
    customQ = []
    customQ.append(rootNode)
    while customQ:
        root = customQ.pop()
        if root.data == searchItem:
            return "Found"
        if root.leftChild:
            customQ.append(root.leftChild)
        if root.rightChild:
            customQ.append(root.rightChild)
    return "Not Found"


def insertion(rootNode, nodeValue):
    """
    time and space complexity is O(n)
    """
    if not rootNode:
        return
    customQ = []
    customQ.append(rootNode)
    while customQ:
        root = customQ.pop()
        if root.leftChild:
            customQ.append(root.leftChild)
        else:
            root.leftChild = TreeNode(nodeValue)
            return
        if root.rightChild:
            customQ.append(root.rightChild)
        else:
            root.rightChild = TreeNode(nodeValue)
            return


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


def deleteNodeBST(rootNode, node):
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


def deleteEntireBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "Success"


newBT = TreeNode("Drinks")
cold = TreeNode("Cold")
hot = TreeNode("Hot")
newBT.leftChild = cold
newBT.rightChild = hot
# preOrderTraversal(newBT)
# inOrderTraversal(newBT)
# postOrderTraversal(newBT)
# levelOrderTraversal(newBT)
print(search(newBT, "Cold"))
insertion(newBT, "Tea")
insertion(newBT, "Coffee")
insertion(cold, "Soda")
levelOrderTraversal(newBT)

deleteNodeBST(newBT, "Soda")
print("-----> After deletion")
levelOrderTraversal(newBT)

deleteEntireBT(newBT)
levelOrderTraversal(newBT)
