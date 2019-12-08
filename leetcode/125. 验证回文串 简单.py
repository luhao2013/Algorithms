"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
"""


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ## 解法1
        # import re
        # s = re.sub("[^A-Za-z0-9]","",s).lower()
        # #print(s)
        # s_inverse = s[::-1]
        # return s == s_inverse

        # #解法2
        # s = "".join(filter(str.isalnum, s)).lower()
        # return s == s[::-1]

        # 解法3 双指针
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1

        return True




if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    test = Solution()
    print(test.isPalindrome(s))