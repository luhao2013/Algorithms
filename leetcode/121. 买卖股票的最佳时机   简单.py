"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""
class Solution:
    def maxProfit(self, prices):
        # 解法1
        # 后面最大值减前面的最小值
        # 对于每一天来说，它能得到的最大利益就是它和之前最低点的差
        if len(prices) <= 1:
            return 0
        max_price = 0
        low = prices[0]
        for i in range(1, len(prices)):
            max_price = max(prices[i] - low, max_price)
            low = min(low, prices[i])
        return max_price

        # 解法2
        # 动态规划


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    test = Solution()
    print(test.maxProfit(prices))