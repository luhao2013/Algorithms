"""
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 解法1 暴力求解 递归

        # 解法2 动态规划
        # 状态定义：DP[i][2] 0-->i 正数乘积最大和负数乘积最小
        # 存储0 到 i-1 每个位置的最大值，最后求max
        # 下面的状态转移方程应该是少了和当前位置的值比较，为了是可以重启动，比如0，1
        # 就可以舍弃0用1
        # 状态转移方程：DP[i+1][0] = DP[i][0] * a[i+1], if a[i+1]>=0
        #                           DP[i][1] * a[i+1], if a[i+1]《0
        #              DP[i+1][0] = DP[i][1] * a[i+1], if a[i+1]>=0
        #                           DP[i][0] * a[i+1], if a[i+1]《0

        # 这道题的重点就是要把前一次的最大值和最小值都保存下来
        if not nums:
            return 0
        # 最大值和负最大值都要保存下来
        # index在0为Max在1为Min，两个子数组迭代时滚动
        dp = [[0 for _ in range(2)] for _ in range(2)]

        dp[0][1], dp[0][0], res = nums[0], nums[0], nums[0]  # 最大值，最小值，最后结果

        for i in range(1, len(nums)):  # 遍历nums数组
            x, y = i % 2, (i - 1) % 2  # 滚动数组，x和y在0和1中滚动
            dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            res = max(res, dp[x][0])

        return res

        # 另一种写法
#         if not nums:
#             return 0

#         res, curMax, curMin = nums[0], nums[0], nums[0]

#         for i in range(1, len(nums)):
#             num = nums[i]
#             curMax, curMin = curMax * num, curMin * num
#             curMin, curMax = min(curMax, curMin, num), max(curMax, curMin, num)
#             if curMax > res:
#                 res = curMax

#         return res
