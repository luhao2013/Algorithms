"""
统计一个数字在排序数组中出现的次数。
"""


# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0

        count = 0
        number = 0
        first = self.getFirstK(data, k)
        last = self.getLastK(data, k)
        if first > -1 and last > -1:
            number = last - first + 1

        return number

    def getFirstK(self, data, k):
        start = 0
        end = len(data) - 1

        index = -1
        while start <= end:
            mid = (start + end) // 2
            if data[mid] > k:
                end = mid - 1
            elif data[mid] < k:
                start = mid + 1
            else:
                if (mid > 0 and data[mid - 1] != k) or mid == 0:
                    return mid
                else:
                    end = mid - 1
        return index

    def getLastK(self, data, k):
        start = 0
        end = len(data) - 1

        index = -1
        while start <= end:
            mid = (start + end) // 2

            if data[mid] > k:
                end = mid - 1
            elif data[mid] < k:
                start = mid + 1
            else:
                if (mid < len(data) - 1 and data[mid + 1] != k) or mid == len(data) - 1:
                    return mid
                else:
                    start = mid + 1
        return index
