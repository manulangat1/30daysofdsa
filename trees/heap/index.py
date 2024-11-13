class Heap:
    def __init__(self, size) -> None:
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1


def peekOfHeap(rootNode):
    if not rootNode:
        return
    return rootNode.customList[1]


def sizeOfHeap(rootNode):
    if not rootNode:
        return
    return rootNode.heapSize


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    for i in range(1, (rootNode.heapSize + 1)):
        print(rootNode.customList[i])


def heapifyTreeInsert(rootNode, index, heapType):
    parentIdx = int(index / 2)
    if index <= 1:
        return
    if heapType == "min":
        if rootNode.customList[index] < rootNode.customList[parentIdx]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIdx]
            rootNode.customList[parentIdx] = temp
        heapifyTreeInsert(rootNode, parentIdx, heapType)
    elif heapType == "max":
        if rootNode.customList[index] > rootNode.customList[parentIdx]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIdx]
            rootNode.customList[parentIdx] = temp
        heapifyTreeInsert(rootNode, parentIdx, heapType)


def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "Full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "Value inserted successfully"


def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    else:
        if heapType == "min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        heapifyTreeExtract(rootNode, swapChild, heapType)


def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return
    extractNode = rootNode.customList[1]
    rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
    rootNode.heapSize -= 1
    heapifyTreeExtract(rootNode, 1, heapType)
    return extractNode


newBinaryHeap = Heap(5)
insertNode(newBinaryHeap, 4, "max")
insertNode(newBinaryHeap, 5, "max")
insertNode(newBinaryHeap, 2, "max")
insertNode(newBinaryHeap, 1, "max")

print(extractNode(newBinaryHeap, "max"))
print("--->")
print(levelOrderTraversal(newBinaryHeap))
