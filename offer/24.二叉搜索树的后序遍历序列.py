"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果，如果是则返回True
否则返回False。假设输入的数组的任意两个数字都不相同。
"""


# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False

        length = len(sequence)
        root = sequence[length - 1]

        i = 0
        while sequence[i] < root:
            i += 1

        # 右子树发现小的就有问题
        j = i
        while j < length - 1:
            if sequence[j] < root:
                return False
            j += 1

        # i>0说明有左子树
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])

        # j != i说明有右子树
        right = True
        if i != j:
            right = self.VerifySquenceOfBST(sequence[i:length - 1])

        return left and right
