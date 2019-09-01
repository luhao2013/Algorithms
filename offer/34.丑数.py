"""
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，
因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""

# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        array = [0] * index
        array[0] = 1
        nextUglyIndex = 1

        mult2 = 0
        mult3 = 0
        mult5 = 0

        while nextUglyIndex < index:
            min_num = min(array[mult2] * 2, array[mult3] * 3, array[mult5] * 5)
            array[nextUglyIndex] = min_num

            while array[mult2] * 2 <= min_num:
                mult2 += 1
            while array[mult3] * 3 <= min_num:
                mult3 += 1
            while array[mult5] * 5 <= min_num:
                mult5 += 1

            nextUglyIndex += 1
        return array[-1]
