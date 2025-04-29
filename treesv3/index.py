"""
IS A  non linear DS with hierachial rlships between its elements without having any cycle.
    Properties:
        1. Represents hierachial data.
        2. Each node has 2 components: data and link to its sub category.

"""


class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    # def __str__(self, level=0):
    #     ret = " " * level + str(self.data) + "\n"
    #     for child in self.children:
    #         ret += child.__str__(level + 1)
    #     return ret

    def __str__(self, level=0):
        ret = "  " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self, TreeNode):
        self.children.append(TreeNode)


tree = TreeNode("Drinks")
print(tree)
cold = TreeNode("Cold")
hot = TreeNode("Hot")
tree.addChild(cold)
# tree.addChild(hot)
print("---------->")
print(tree)
