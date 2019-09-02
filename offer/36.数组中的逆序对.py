"""
题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
输入描述:
题目保证输入的数组中没有的相同的数字

数据范围：

	对于%50的数据,size<=10^4

	对于%75的数据,size<=10^5

	对于%100的数据,size<=2*10^5
"""


# 1.没有传引用，复杂度高，通过75%
# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if len(data) <= 1:
            return 0
        self.data = data
        return self.merge_sort(0, len(start - 1)) % 1000000007

    def merge_sort(self, start, end):
        if len(data) <= 1:
            return 0, data
        mid = len(data) // 2
        left_count = self.merge_sort(start, mid)
        right_count = self.merge_sort(mid + 1, start)
        cur_count = self.merge(start, mid, end)
        return left_count + right_count + cur_count

    def merge(self, start, mid, end):
        count = 0
        res = [0] * (end - start - 1)
        left_index = mid
        right_index = end
        res_index = end
        while left_index >= 0 and right_index >= 0:
            if left_array[left_index] <= right_array[right_index]:
                res[res_index] = right_array[right_index]
                right_index -= 1
                res_index -= 1
            else:
                res[res_index] = left_array[left_index]
                left_index -= 1
                res_index -= 1
                count = count + right_index + 1
        for i in range(left_index, -1, -1):
            res[res_index] = left_array[i]
            res_index -= 1
        for i in range(right_index, -1, -1):
            res[res_index] = right_array[i]
            res_index -= 1

        self.data[start:end + 1] = res

        return count

# 2.传引用，完全通过
# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if len(data) <= 1:
            return 0
        self.data = data
        return self.merge_sort(0, len(data) - 1) % 1000000007

    def merge_sort(self, start, end):
        if start == end:
            return 0
        mid = (start + end) // 2
        left_count = self.merge_sort(start, mid)
        right_count = self.merge_sort(mid + 1, end)
        cur_count = self.merge(start, mid, end)
        return left_count + right_count + cur_count

    def merge(self, start, mid, end):
        count = 0
        res = [0] * (end - start + 1)
        left_index = mid
        right_index = end
        res_index = len(res) - 1
        while left_index >= start and right_index >= mid + 1:
            if self.data[left_index] <= self.data[right_index]:
                res[res_index] = self.data[right_index]
                right_index -= 1
                res_index -= 1
            else:
                res[res_index] = self.data[left_index]
                left_index -= 1
                res_index -= 1
                count = count + right_index - mid
        for i in range(left_index, start - 1, -1):
            res[res_index] = self.data[i]
            res_index -= 1
        for i in range(right_index, mid, -1):
            res[res_index] = self.data[i]
            res_index -= 1
        self.data[start:end + 1] = res
        return count
