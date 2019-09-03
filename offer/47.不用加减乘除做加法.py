"""
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
"""


# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:
            add = num1 ^ num2  # 不考虑进位的加法
            # 使用位运算，Python中大整数会自动处理，因此对carry需要加个判断
            # 在Python内部对整数的处理分为普通整数和长整数，普通整数长度为机器位长，
            # 通常都是32位，超过这个范围的整数就自动当长整数处理，而长整数的范围几乎完全没限制
            # 所以long类型运算内部使用大数字算法实现，可以做到无长度限制。
            # 但是向左一位的话，那么最后低位会变成高位
            # 因为在Python中，对于超出32位的大整数，会自动进行大整数的转变，
            # 这就导致了在右移位过程中，不会出现移到了0的情况，也就会造成了死循环。
            carry = 0xFFFFFFFF & ((num1 & num2) << 1)
            # 判断a为正数还是负数
            carry = -(~(carry - 1) & 0xFFFFFFFF) if carry > 0x7FFFFFFF else carry
            num1 = add
            num2 = carry
        return num1
