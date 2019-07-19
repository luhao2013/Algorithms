"""
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释:
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 解法1，暴力求解
        # DFS BFS

        # 解法2动态规划 O(mn)
        # word1的前i个字符==》word2前j 最少步数
        # DP[i,j] = DP[i-1][j-1] if w1[i] == w2[j]
        #           1 + Min(DP[i-1][j],DP[i,j-1], DP[I-1.J-1])  else  三种操作的最小值
        m, n = len(word1), len(word2)
        # 这个状态定义像是从左下角到右下角的动态规划
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  # (m, n)矩阵

        # 初始化
        for i in range(m + 1):
            dp[i][0] = i  # 全部删除
        for j in range(n + 1):
            dp[0][j] = j  # 全部插入

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # dp下标要比word下标多1，因为有初始化
                # 如果word1[i-1] == word2[j-1]，不需要操作，否则需要增dp[i-1][j] + 1
                # 删dp[i][j-1]+1，替换dp[i-1][j-1]+1，三者最小的
                dp[i][j] = min(dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1),
                               dp[i - 1][j] + 1,  # insert
                               dp[i][j - 1] + 1)  # delete
        return dp[m][n]
