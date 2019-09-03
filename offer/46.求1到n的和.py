"""
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""


# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        result = n
        # 注意and与&的区别
        temp = n > 0 and self.Sum_Solution(n - 1)

        return result + temp
