"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 解法1 递归 从上往下想，求出所有路径和 O(2^n)
        # 改进，使用记忆化备忘录

        # 贪心法不合适
        # 解法2 动态规划，从下往上想
        # 状态的定义：DP[i,j]:bottom-->(i,j)路径和的最小值 将往后余生的值都计算出来了
        # 状态方程：DP[i,j] = min(DP[i+1,j], DP[i+1,j+1]) + Triangle[i, j]
        # 起始值 最下面一行 DP[m-1, j] = Triangle[m-1, j]
        # O(mn) 有点像归并排序以及二叉树求最小值从下往上的思想
        if not triangle:
            return 0

        # 节省空间，result只使用最下面一层的一维数据即可
        result = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):  # 从倒数第二层向上
            for j in range(len(triangle[i])):  # 本层遍历
                result[j] = min(result[j], result[j+1]) + triangle[i][j]
        return result[0]  # 到第一行，只剩一个数值
