"""
题目描述
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
"""


# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        small = 1
        big = 2

        middle = (1 + tsum) // 2
        curSum = small + big

        res = []
        while small < middle:
            if curSum == tsum:
                print(small, big, curSum)
                res.append([i for i in range(small, big + 1)])
                big += 1
                curSum += big
            elif curSum < tsum:
                big += 1
                curSum += big
            else:
                curSum -= small
                small += 1

        return res


# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        small = 1
        big = 2

        middle = (1 + tsum) // 2
        curSum = small + big

        res = []
        while small < middle:
            if curSum == tsum:
                res.append([i for i in range(small, big + 1)])

            while curSum > tsum and small < middle:
                curSum -= small
                small += 1
                if curSum == tsum:
                    res.append([i for i in range(small, big + 1)])

            big += 1
            curSum += big
        return res
