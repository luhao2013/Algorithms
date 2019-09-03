"""
题目描述
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，
第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。
"""


# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.count = 0
        self.char_dict = {}
        self.char_set = set()
    def FirstAppearingOnce(self):
        # write code here
        if not self.char_dict:
            return "#"
        return min(self.char_dict, key=self.char_dict.get)
    def Insert(self, char):
        # write code here
        self.count += 1
        if char not in self.char_set:
            if char not in self.char_dict:
                self.char_dict[char] = self.count
            else:
                self.char_set.add(char)
                del self.char_dict[char]
