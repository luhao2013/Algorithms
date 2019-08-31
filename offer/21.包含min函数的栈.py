"""
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min函数。
在该栈中，调用min、push及pop的时间复杂度都是O(1)
"""

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.assist = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.assist:
            self.assist.append(node)
        else:
            if node < self.assist[-1]:
                self.assist.append(node)
            else:
                self.assist.append(self.assist[-1])

    def pop(self):
        # write code here
        if not self.stack:
            raise Exception('Stack Empety')
        self.stack.pop()
        self.assist.pop()

    def top(self):
        # write code here
        if not self.stack:
            raise Exception('Stack Empety')
        return self.stack[-1]

    def min(self):
        # write code here
        if not self.stack:
            raise Exception('Stack Empety')
        return self.assist[-1]