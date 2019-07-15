"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 买入算一次交易，卖出不算

        if not prices:
            return 0

        res = 0
        # 三维分别表示：天数, 交易次数，拥有股票的状态（没有任何交易状态，不持有状态，持有状态）
        profit = [[[0 for _ in range(2)] for _ in range(3)] for i in range(len(prices))]
        for i in range(3):
            profit[0][i][0], profit[0][i][1] = 0, -prices[0]

        for i in range(1, len(prices)):
            for k in range(0, 3):
                if k == 0:  # 如果还没有任何交易
                    # 当前没有股票,买入算一次交易，卖出不算
                    # profit[i][k][0] = max(profit[i-1][k][0], 0)
                    profit[i][k][0] = 0
                    # 当前拥有股票
                    # profit[i][k][1] = max(profit[i-1][k][1], 0)
                    profit[i][k][1] = 0
                else:
                    # 当前没有股票,买入算一次交易，卖出不算，1：前一天没有股票，2：前一天有股票今天卖出 因为是卖出所以不算交易，没有交易前后的k都一致
                    profit[i][k][0] = max(profit[i - 1][k][0], profit[i - 1][k][1] + prices[i])
                    # 当前拥有股票，1：前一天有股票，2：前一天没有股票今天买入
                    profit[i][k][1] = max(profit[i - 1][k][1], profit[i - 1][k - 1][0] - prices[i])

            res = max([max(i) for i in profit[-1]])

        return res

        # first_buy, first_sell, second_buy, second_sell = -sys.maxsize, 0, -sys.maxsize, 0
        # for price in prices:
        #     first_buy = max(first_buy, -price)  # 第一次买入手上的钱
        #     first_sell = max(first_sell, price+first_buy)  # 第一次卖出手上的钱
        #     second_buy = max(second_buy, first_sell-price)  # 第二次买入手上的钱
        #     second_sell = max(second_sell, price+second_buy)  # 第二次卖出手上的钱
        # return second_sell
