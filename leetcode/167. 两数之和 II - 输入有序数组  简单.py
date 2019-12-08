"""
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 1. 哈希表
        nums_dict = {}
        for index, value in enumerate(numbers):
            if value not in nums_dict:
                nums_dict[target-value] = index
            else:
                return [nums_dict[value]+1, index+1]

        # 2. 二分搜索
        def bi_search(left, right, arr, target):
            while left <= right:
                mid = (left + right) // 2
                # print(mid, target)
                if arr[mid] < target:
                    left = mid + 1
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1

        length = len(numbers)
        for index, value in enumerate(numbers):
            index2 = bi_search(index + 1, length - 1, numbers, target - value)
            if index2 != -1:
                return [index + 1, index2 + 1]
        return []

        # 3 双指针法 从左到右和从右到左
        l = 0
        r = len(numbers)-1
        while l<r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1