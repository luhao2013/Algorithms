"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        self.pre = None  # 必须要用全局变量，或者是传地址或引用

        self.core(pRootOfTree)
        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left
        return pRootOfTree

    def core(self, root):
        if not root:
            return None
        # 中序遍历
        if root.left:
            self.core(root.left)

        if self.pre:
            self.pre.right = root
        root.left = self.pre
        self.pre = root

        if root.right:
            self.core(root.right)
