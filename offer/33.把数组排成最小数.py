"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""


# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""

        # 思路: Python中不需要考虑大整数，需要自己定义一个数组排序规则，直接调用库函数就可以
        def cmp(a, b):
            if str(a) + str(b) < str(b) + str(a):
                return -1
            else:
                return 1
            # return int(str(a)+str(b)) - int(str(b)+str(a))

        return int(''.join([str(num) for num in sorted(numbers, cmp=cmp)]))
