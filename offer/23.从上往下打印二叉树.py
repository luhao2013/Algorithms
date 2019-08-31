"""
从上往下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []

        array = [[root], []]
        flag = 1
        res = []

        while array[1 - flag]:
            array[flag] = []
            for node in array[1 - flag]:
                res.append(node.val)
                if node.left:
                    array[flag].append(node.left)
                if node.right:
                    array[flag].append(node.right)
            flag = 1 - flag
        return res

