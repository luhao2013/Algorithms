"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result_length = 0
        length = len(s)
        # 标识i到j是否是回文串
        dp = [[0 for _ in range(length)] for _ in range(length)]
        result = ''

        # # 初始化条件
        # for i in range(length):  # i-j<=1为1
        #     dp[i][i] = 1
        #     if i < length-1 and s[i] == s[i+1]:
        #         dp[i][i+1] = 1

        # 要先对行进行遍历
        for j in range(length):  # 列
            for i in range(j + 1):  # 行
                # 初始化条件,主要是i到j长度为1-2的回文判定
                if j - i <= 1:
                    if s[i] == s[j]:
                        dp[i][j] = 1
                        if result_length <= j - i + 1:
                            result_length = j - i + 1
                            result = s[i:j + 1]
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = 1
                        if result_length <= j - i + 1:
                            result_length = j - i + 1
                            result = s[i:j + 1]
        return result
