"""
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        # 后序遍历
        return self.core(pRoot) >= 0

    def core(self, pRoot):
        if not pRoot:
            return 0

        left = self.core(pRoot.left)
        right = self.core(pRoot.right)

        if left < 0 or right < 0 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
