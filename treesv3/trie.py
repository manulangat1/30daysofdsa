"""
    Is a tree based data structure that organizes information in a hierachy. ]
Properties.
    1. Used to store or search strings in a space and time efficient way.
    2. Any node in trie can store non repetitive multiple characters.
    3. Every node  stores link of the next character of the string.
    4. Every node keeps track of end of string.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root

        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.endOfString = True
        print("Successfully inserted")

    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node
        if currentNode.endOfString == True:
            return True
        else:
            return False


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


# def deleteString(root, word, index):
#     ch = word[index]
#     currentNode = root.children.get(ch)
#     canThisNodeBeDeleted = False

#     if len(currentNode.children) > 1:
#         deleteString(currentNode, word, index + 1)
#         return False
#     if index == len(word) - 1:
#         if len(currentNode.children) >= 1:
#             currentNode.endOfString = False
#             return False
#         else:
#             root.children.pop(ch)
#             return True
#     if currentNode.endOfString == True:
#         deleteString(currentNode, word, index)
#         return False

#     canThisNodeBeDeleted = deleteString(currentNode, word, index + 1)
#     if canThisNodeBeDeleted == True:
#         root.children.pop(ch)
#         return True
#     else:
#         return False


newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Apple")
print(newTrie.searchString("Appk"))
print(newTrie.searchString("App"))
print(deleteString(newTrie, "App", 0))
