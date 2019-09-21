"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # # 1. 暴力解
        # max_area = 0
        # for index1 in range(len(height)-1):
        #     for index2 in range(index1, len(height)):
        #         temp = (index2-index1) * min(height[index1], height[index2])
        #         if temp > max_area:
        #             max_area = temp
        # return max_area

        # 2. 双指针法
        max_area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            max_area = max(max_area, (r - l) * min(height[r], height[l]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
