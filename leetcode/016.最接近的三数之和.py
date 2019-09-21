"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import sys


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #         # 自己写的
        #         if len(nums) < 3:
        #             return []
        #         min_num = sys.maxsize
        #         nums.sort()
        #         res = []
        #         for index1 in range(len(nums)-2):
        #             left_index = index1 + 1
        #             right_index = len(nums) - 1
        #             while left_index < right_index:
        #                 temp = abs(nums[index1] + nums[left_index] + nums[right_index]-target)
        #                 if temp < min_num:
        #                     min_num = temp
        #                     res = (nums[index1], nums[left_index], nums[right_index])

        #                 if nums[left_index] + nums[right_index] < target-nums[index1]:
        #                     left_index += 1
        #                 else:
        #                     right_index -= 1
        #         return sum(res)

        # 优化
        nums.sort()
        diff = 2147483647
        res = target
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == target:  # 相等就是最接近直接返回
                    return s
                elif s < target:
                    if target - s < diff:
                        diff = target - s
                        res = s
                    left += 1
                    # 相同的值就跳过
                    while left + 1 < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    if s - target < diff:
                        diff = s - target
                        res = s
                    right -= 1
                    while right - 1 > left and nums[right] == nums[right + 1]:
                        right -= 1
        return res
