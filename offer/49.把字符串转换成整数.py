"""
题目描述
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0
示例1
输入
+2147483647
    1a33
输出
2147483647
    0
"""


# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        # 遇到不符合数字返回0

        if not s:
            return 0
        flag = 1
        count = 0
        for index, char in enumerate(list(s)):
            if index == 0 and char == "-":
                flag = -1
                continue
            elif index == 0 and char == "+":
                continue
            if '0' <= char <= '9':
                count = count * 10 + int(char)
                continue
            else:
                return 0
        count = flag * count
        return count
