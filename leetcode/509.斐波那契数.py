"""
斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
给定 N，计算 F(N)。

 

示例 1：

输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
示例 2：

输入：3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
示例 3：

输入：4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3.
 

提示：

0 ≤ N ≤ 30

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fibonacci-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 解法1 递归
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        return self.fib(N - 1) + self.fib(N - 2)

# 解法2 带备忘录的递归
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.memory = [0] * (N + 1)
        return self.helper(N)

    def helper(self, N):
        if N <= 1:
            return N
        if not self.memory[N]:
            self.memory[N] = self.helper(N - 1) + self.helper(N - 2)
        return self.memory[N]


# 解法三、动态规划，最最简单的动态规划，递归+记忆话==》递推
# 有了上一步「备忘录」的启发，我们可以把这个「备忘录」独立出来成为一张表，
# 就叫做 DP table 吧，在这张表上完成「自底向上」的推算岂不美哉！
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        memory = [0] * (N+1)
        memory[1] = 1
        for i in range(2, N+1):
            memory[i] = memory[i-1] + memory[i-2]  # dp状态转移方程，递推公式
        return memory[N]