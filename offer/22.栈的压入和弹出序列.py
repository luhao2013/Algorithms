"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序
"""


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []

    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV) != len(popV):
            return False

        for i in pushV:
            self.stack.append(i)
            while len(self.stack) and self.stack[-1] == popV[0]:
                self.stack.pop()
                popV.pop(0)
        if len(self.stack):
            return False
        return True
