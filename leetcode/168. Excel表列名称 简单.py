"""
给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
示例 1:

输入: 1
输出: "A"
示例 2:

输入: 28
输出: "AB"
示例 3:

输入: 701
输出: "ZY"
"""
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        while n:
            # 每次都是0-25，就像0-9不会是1-10
            n -= 1  # 如果没有 n -= 1；这条语句的话 例如52 的余26为0 那最后得出的结果是错的。
            temp = n % 26
            result = chr(ord('A')+temp) +result
            n = (n-temp)/26
        return result