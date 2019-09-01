"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""


# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0

        count = 0
        cur = numbers[0]
        for num in numbers:
            if count == 0:
                cur = num
                count = 1
            elif num == cur:
                count += 1
            else:
                count -= 1
        if numbers.count(cur) <= len(numbers) // 2:
            return 0
        else:
            return cur


# 快排思想
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0

        length = len(numbers)
        mid = length // 2
        start = 0
        end = length - 1
        index = self.Partition(numbers, start, end)
        while index != mid:
            if index < mid:
                index = self.Partition(numbers, index + 1, end)
            else:
                index = self.Partition(numbers, start, index - 1)
        cur = numbers[mid]

        if numbers.count(cur) <= len(numbers) // 2:
            return 0
        else:
            return cur

    def Partition(self, numbers, left, right):
        pivot = numbers[left]
        while left < right:
            while left < right and numbers[right] >= pivot:  # 判断大小的时候一定要有等号
                right -= 1
            numbers[left] = numbers[right]
            while left < right and numbers[left] <= pivot:
                left += 1
            numbers[right] = numbers[left]
        numbers[left] = pivot
        return left
