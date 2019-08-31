"""
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.res = []
        self.one_res = []
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        self.core(root, expectNumber)
        return self.res

    def core(self, root, expectNumber):

        if root == None:
            return

        self.one_res.append(root.val)
        curNumber = expectNumber - root.val
        # 不能进入空节点判断，因为一共叶节点的会有两个子节点，会重复插入
        if curNumber == 0 and root.right == None and root.left == None:
            i = 0
            while i < len(self.res):
                if len(self.one_res) > len(self.res[i]):
                    break
                i += 1
            self.res.insert(i, [val for val in self.one_res])

        if root.left:
            self.core(root.left, curNumber)
        if root.right:
            self.core(root.right, curNumber)
        self.one_res.pop()
