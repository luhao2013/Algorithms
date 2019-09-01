"""
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
"""


# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n <= 0:
            return 0
        if n < 10:
            return 1
        digit = self.get_digits(n)  # 位数
        high = int(str(n)[0])  # 最高位
        low = n - high * 10 ** (digit - 1)  # 去掉最高位的低位

        # 如果是21345，先考虑四位数，再考虑1346到9999四位数的，剩下就是递归了

        # 最高位1的个数
        numFirstDigit = 0
        # 假设n是112345
        if high == 1:
            numFirstDigit = low + 1
            # 假设最高位大于1
        else:
            numFirstDigit = 10 ** (digit - 1)

            # numOtherDigit是1346到21345除了第一位之外的数位中的数目,有两万个，所以可以这么乘
        numOtherDigits = high * (digit - 1) * 10 ** (digit - 2)

        numRecursive = self.NumberOf1Between1AndN_Solution(low)
        return numFirstDigit + numOtherDigits + numRecursive

    def get_digits(self, n):
        count = 0
        while n:
            n = n // 10
            count += 1
        return count
