"""
left is less than or equal to its parents node value.
right is greater than its parents node value
"""


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertNode(rootNode, nodeValue):
    """
    Time complexity is O(log N)
    """
    if rootNode.data == None:
        rootNode.data = nodeValue
        return
    if nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def levelOrder(rootNode):
    if not rootNode:
        return
    customQ = [rootNode]
    while customQ:
        node = customQ.pop()
        print(node.data)
        if node.leftChild:
            customQ.append(node.leftChild)
        if node.rightChild:
            customQ.append(node.rightChild)


# def search(rootNode, searchValue):
#     # if not rootNode:
#     #     return
#     if rootNode.data == searchValue:
#         return f"Found at {rootNode.data} "
#     if searchValue <= rootNode.data:
#         # if rootNode.leftChild.data == searchValue:
#         #     return f"Found at {rootNode.data} "

#         search(rootNode.leftChild, searchValue)
#     else:
#         # if rootNode.rightChild.data == searchValue:
#         #     return f"Found at {rootNode.data} "
#         search(rootNode.rightChild, searchValue)
#     return "Not Found"


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


newBST = BSTNode(1)
insertNode(newBST, 10)
insertNode(newBST, 5)
insertNode(newBST, 40)
print("here --->")
preOrderTraversal(newBST)
# levelOrder(newBST)
print("search --------->")
print(search(newBST, 41))
