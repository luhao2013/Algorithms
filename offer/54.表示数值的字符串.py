"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""


# 注意每一次遇到非字母都要判断是否在最后一位
# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s:
            return False

        flag = True
        index = 0

        # 判断第一位是否为正负号
        if s[0] in ['+', '-']:
            flag = False
            index += 1
        if index == len(s):
            return False

        index = self.scan_digits(s, index)

        if index < len(s):
            # 浮点型
            if s[index] == '.':
                index += 1
                if index == len(s):
                    return False
                index = self.scan_digits(s, index)
                if index == len(s):
                    return True
                if s[index] in ['e', 'E']:
                    return self.isExponential(s, index)
            # 整数
            elif s[index] in ['e', 'E']:
                return self.isExponential(s, index)
            # 遇到了其他字母
            else:
                return False
        return index == len(s)

    def scan_digits(self, string, index):
        while index < len(string):
            if string[index] <= '9' and string[index] >= '0':
                index += 1
            else:
                break
        return index

    def isExponential(self, s, index):
        index += 1
        # e或E是末尾
        if index == len(s):
            return False

        if s[index] in ['+', '-']:
            index += 1

        # +或-是末尾
        if index == len(s):
            return False

        index = self.scan_digits(s, index)
        # 判断是否到达末尾
        return True if index == len(s) else False

