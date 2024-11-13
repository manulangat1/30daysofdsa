class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insertString(self, word):
        currNode = self.root
        for i in word:
            ch = i
            node = currNode.children.get(ch)
            if node == None:
                node = TrieNode()
                currNode.children.update({ch: node})
            currNode = node
        currNode.endOfString = True
        print("Successfully inserted")

    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if not node:
                return False
            currentNode = node
        return currentNode.endOfString


def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index + 1)
        return False
    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True

    if currentNode.endOfString:
        deleteString(currentNode, word, index + 1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, word, index + 1)
    if canThisNodeBeDeleted:
        root.children.pop(ch)
        return True
    else:
        return False


newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Apple")
deleteString(newTrie.root, "App", 0)
print(newTrie.searchString("App"))
