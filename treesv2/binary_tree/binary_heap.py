class Heap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1


def peekofHeap(rootNode):
    if not rootNode:
        return

    #  no deletion, just returning.
    return rootNode.customList[1]


def sizeOfHeap(rootNode):
    if not rootNode:
        return
    return rootNode.heapSize


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        print("Looping")
        for i in range(1, rootNode.heapSize + 1):
            print(i)
            print(rootNode.customList[i])


def heapifyTreeInsert(rootNode, index, heapType):
    parentIdx = int(index / 2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIdx]:
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
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "Success"


newBinaryHeap = Heap(5)
print(sizeOfHeap(newBinaryHeap))
insertNode(newBinaryHeap, 4, "Min")
insertNode(newBinaryHeap, 5, "Min")
insertNode(newBinaryHeap, 2, "Min")
insertNode(newBinaryHeap, 1, "Min")
levelOrderTraversal(newBinaryHeap)
