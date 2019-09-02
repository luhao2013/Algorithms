"""
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置,
如果没有则返回 -1（需要区分大小写）.
"""


# 1.使用哈希字典，O(n)
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        has_dict = dict()
        for index, char in enumerate(s):
            if char not in has_dict:
                has_dict[char] = index
            else:
                has_dict[char] = float('inf')

        return min(has_dict.values())
