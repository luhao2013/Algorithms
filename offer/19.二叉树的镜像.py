"""
请完成一个函数，输入一个二叉树，该函数输出它的镜像。
"""

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def mirrorRecursively(curr_node):
    if not curr_node:
        return
    if not curr_node.left and not curr_node.right:
        return

    curr_node.left, curr_node.right = curr_node.right, curr_node.left

    if curr_node.left:
        mirrorRecursively(curr_node.left)

    if curr_node.right:
        mirrorRecursively(curr_node.right)
