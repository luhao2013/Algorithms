"""
题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，
输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。
"""


# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        res = []
        left = 0
        right = len(array) - 1

        while left < right:
            if array[left] + array[right] == tsum:
                res.append([array[left], array[right]])
                left += 1
            elif array[left] + array[right] < tsum:
                left += 1
            else:
                right -= 1
        if not res:
            return []
        index = 0
        max_prod = float('inf')
        for i in range(len(res)):
            if res[i][0] * res[i][1] < max_prod:
                max_prod = res[i][0] * res[i][1]
                index = i
        return res[index]
