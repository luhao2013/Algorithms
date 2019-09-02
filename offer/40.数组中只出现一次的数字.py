"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""


# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if array == None and length < 2:
            return

        resultOR = 0
        for i in range(len(array)):
            resultOR ^= array[i]

        indexOf1 = self.findFirstBitIs1(resultOR)

        num1 = 0
        num2 = 0
        for i in range(len(array)):
            if self.isBit1(array[i], indexOf1):
                num1 ^= array[i]
            else:
                num2 ^= array[i]
        return (num1, num2)

    def findFirstBitIs1(self, num):
        index = 0
        while num & 1 == 0:
            num = num >> 1
            index += 1
        return index

    def isBit1(self, num, index):
        num = num >> index
        return num & 1
