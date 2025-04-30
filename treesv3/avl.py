"""
- Is a self balancing BST tree where diff btwn heights of left and right subtrees cannot be more than 1 for all the nodes.
"""


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

    def __str__(self):
        return str(self.data)


newAVL = AVLNode(10)


# pre, in and post order is the same as the other implementations.


def levelOrder(rootNode):
    if not rootNode:
        return

    customQ = [rootNode]
    while customQ:
        root = customQ.pop()
        print(root.data)
        if root.leftChild:
            customQ.append(root.leftChild)
        if root.rightChild:
            customQ.append(root.rightChild)


def searchNode(rootNode, searchItem):
    print(rootNode, rootNode.data)
    # if rootNode.data == searchItem:
    #     return True
    # if searchItem < rootNode.data:
    #     searchNode(rootNode.leftChild, searchItem)
    # else:
    #     if rootNode.rightChild and rootNode.rightChild.data == searchItem:
    #         return True
    #     else:
    #         searchNode(rootNode.rightChild, searchItem)
    # return False


levelOrder(newAVL)
print(searchNode(newAVL, 11))
