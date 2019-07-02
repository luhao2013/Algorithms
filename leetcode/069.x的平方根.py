"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x == 0) or (x == 1):
            return x
        # 1. 二分法
        left = 1
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid == (x // mid):
                return mid
            elif mid > (x // mid):
                right = mid - 1
            else:
                left = mid + 1
                res = mid  # 取值可能带有小数，left有可能已经大于目标值了

        return res

        # # 2. 牛顿迭代法
        # r = x
        # while r * r > x:
        #     r = (r + x/r) / 2
        # return r