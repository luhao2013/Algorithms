"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""

class Solution:
    def maxProfit(self, prices):
        """
        :param prices: List[int]
        :return: int
        """
        # df = list(map(lambda x: x[0] - x[1], zip(prices[1:], prices[0:])))
        # df = [x for x in df if x > 0]
        # return sum(df)
        if len(prices) <= 1:
            return 0
        k = 2
        profit = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(len(prices))]
        # 促使话
        for i in range(k+1):  # 第一天有的交易次数的状态应该没有的
            profit[0][i][0], profit[0][i][1] = 0, -prices[1]

        for i in range(1, len(prices)):
            for j in range(k+1):
                if k == 0:
                    profit[i][k][0] = max(profit[i-1][k][0], 0)
                    profit[i][k][1] = max(profit[i-1][k][1], 0)
                else:
                    profit[i][k][0] = max(profit[i-1][k][0], profit[i-1][k][1]+prices[i])
                    profit[i][k][1] = max(profit[i-1][k][1], profit[i-1][k][0]-prices[i])
        res = max([max(i) for i in profit[-1]])
        return res
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    test = Solution()
    print(test.maxProfit(prices))