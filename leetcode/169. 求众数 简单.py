"""
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. 暴力计数双重循环

        # 2. 排序，再n/2处的就是结果

        # 3. 分治

        # 4. map
        count_dict = {}
        for i in nums:
            count_dict[i] = count_dict.get(i, 0) + 1
        result = max(count_dict, key=count_dict.get)
        # print(result)
        return result