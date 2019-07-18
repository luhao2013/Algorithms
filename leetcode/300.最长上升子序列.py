"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1.动态规划
        # DP[i]:从头到i元素，最长子序列的长度
        # for i:0-->n-1:
        #   DP[i] = Max{DP[j]} + 1
        #   注：j:0-->i-1 且a[j]<a[i]
        # O(N^2)
        # if not nums:
        #     return 0
        # dp = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j]+1)
        # return max(dp)

        # 2.二分搜索 O(NlogN)
        # nums = [10, 9, 2, 5, 3, 4]
        # 找到最长长度，而非子序列
        if not nums or len(nums) == 1:
            return len(nums)

        result = []
        for i in nums:
            # 二分查找
            low = 0
            high = len(result)
            while low < high:
                mid = (high + low) // 2
                if i <= result[mid]:
                    high = mid
                elif i > result[mid]:
                    low = mid + 1
            if low < len(result):
                result[low] = i
            else:
                result.append(i)
        return len(result)
