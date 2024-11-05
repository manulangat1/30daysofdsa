class TreeNode:
    def __init__(self, data, children=[]) -> None:
        self.data = data
        self.children = children

    def __str__(self, level=0) -> str:
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self, treeNode):
        self.children.append(treeNode)


treeNode = TreeNode("Drinks", [])
cold = TreeNode("Cold", [])
hot = TreeNode("Hot", [])
treeNode.addChild(cold)
treeNode.addChild(hot)
print(treeNode)
