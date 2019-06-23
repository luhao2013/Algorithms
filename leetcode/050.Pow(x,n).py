"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/powx-n
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 帮助理解：
        # https://leetcode-cn.com/problems/powx-n/solution/kuai-su-mi-de-di-gui-yu-fei-di-gui-xie-fa-by-leetc/
        # 1 递归 x^n --> x^(n/2)--> x^(n/4) O(logN)
        # if not n:
        #     return 1
        # if n < 0:
        #     return 1 / self.myPow(x, -n)
        # if n % 2:  # n是奇数的话，用n-1计算
        #     return x * self.myPow(x, n - 1)
        # return self.myPow(x * x, n // 2)

        # 2 非递归
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n % 2:
                # if n & 1:  # 为奇数
                pow *= x
            x *= x
            # n >> 1
            n //= 2
        return pow


s = Solution()
print(s.myPow(2, 7))
