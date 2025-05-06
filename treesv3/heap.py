"""
- Is either Min heap or Max heap.
- It is a complete tree i.e all levels are completely filled except possible the last level and the last level keys are as left as possible.This makes them ideal ti the stored in an array.
"""


class Heap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1


def peekOfHeap(rootNode):
    if not rootNode:
        return
    return rootNode.customList[1]


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    for i in range(1, rootNode.heapSize + 1):
        print(rootNode.customList[i])


# def heapifyTreeInsert(rootNode, index, heapType):
#     parentIdx = int(index / 2)
#     if index <= 1:
#         return
#     if heapType == "Min":
#         if rootNode.customList[index] < rootNode.customList[parentIdx]:
#             temp = rootNode.customList[index]
#             rootNode.customList[index] = rootNode.customList[parentIdx]
#             rootNode.customList[parentIdx] = temp
#         heapifyTreeInsert(rootNode, parentIdx, heapType)
#     elif heapType == "Max":
#         if rootNode.customList[index] > rootNode.customList[parentIdx]:
#             temp = rootNode.customList[index]
#             rootNode.customList[index] = rootNode.customList[parentIdx]
#             rootNode.customList[parentIdx] = temp
#         heapifyTreeInsert(rootNode, parentIdx, heapType)


# def insertNode(rootNode, nodeValue, heapType):
#     if rootNode.heapSize + 1 == rootNode.maxSize:
#         return
#     rootNode.customList[rootNode.heapSize + 1] = nodeValue
#     rootNode.heapSize += 1
#     heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
#     return "Success"


def heapifyTreeInsert(rootNode, index, heapType):
    """
    time and space complexity is O(log N )
    """
    parentIdx = int(index / 2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIdx]:
            # swap the two values
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIdx]
            rootNode.customList[parentIdx] = temp
        heapifyTreeInsert(rootNode, parentIdx, heapType)
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIdx]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIdx]
            rootNode.customList[parentIdx] = temp
        heapifyTreeInsert(rootNode, parentIdx, heapType)


def insertNode(rootNode, nodeValue, heapType):
    """
    time and space complexity is O log N
    """
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    # return "Done"


def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            # pass
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
        elif heapType == "Max":
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        elif heapType == "Max":
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        heapifyTreeExtract(rootNode, swapChild, heapType)


def extractNode(rootNode, heapType):
    """
    time and space complexity is O log N
    """
    if rootNode.heapSize == 0:
        return
    extractNode = rootNode.customList[1]
    rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
    rootNode.heapSize -= 1
    heapifyTreeExtract(rootNode, 1, heapType)
    print(extractNode)
    return extractNode


def deleteEntireBP(rootNode):
    rootNode.customList = None
    rootNode.heapSize = 0


newHeap = Heap(5)
print(peekOfHeap(newHeap))
levelOrderTraversal(newHeap)

insertNode(newHeap, 4, "Min")
insertNode(newHeap, 5, "Min")
insertNode(newHeap, 2, "Min")
insertNode(newHeap, 1, "Min")
print(levelOrderTraversal(newHeap))
extractNode(newHeap, "Min")
print("------------------------------->")
print(levelOrderTraversal(newHeap))

deleteEntireBP(newHeap)

print("------------------------------->")
print(levelOrderTraversal(newHeap))
