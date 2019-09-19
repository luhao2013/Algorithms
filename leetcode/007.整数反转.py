"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 保留数字符号
        sign = 1
        if x < 0:
            sign = -1
            x = sign * x
        elif x == 0:
            return 0

        x_inverse = 0
        while x > 0:
            x_inverse = x_inverse * 10 + x % 10
            x //= 10
        x_inverse = sign * x_inverse

        # 溢出 Python没有32位限制，所以溢出了应该返回0
        long_value = 2
        for _ in range(30):
            long_value *= 2

        if (x_inverse > long_value - 1) or (x_inverse < -1 * long_value):
            return 0

        return x_inverse
