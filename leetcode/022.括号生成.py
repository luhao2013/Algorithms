"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 1. 数学归纳法，n=2是在n=1基础上来的 动态规划
        # https://leetcode-cn.com/problems/generate-parentheses/solution/zui-jian-dan-yi-dong-de-dong-tai-gui-hua-bu-lun-da/
        # 在此题中，动态规划的思想类似于数学归纳法，当知道所有i<n的情况时，我们可以通过某种算法算出i=n的情况。 本题最核心的思想是，考虑i=n时相比n-1组括号增加的那一组括号的位置。
        # 具体思路如下： 当我们清楚所有i<n时括号的可能生成排列后，对与i=n的情况，我们考虑整个括号排列中最左边的括号。 它一定是一个左括号，那么它可以和它对应的右括号组成一组完整的括号"( )"，我们认为这一组是相比n-1增加进来的括号。
        # 那么，剩下n-1组括号有可能在哪呢？ 【这里是重点，请着重理解】 剩下的括号要么在这一组新增的括号内部，要么在这一组新增括号的外部（右侧）。
        # 既然知道了i<n的情况，那我们就可以对所有情况进行遍历： "(" + 【i=p时所有括号的排列组合】 + ")" + 【i=q时所有括号的排列组合】 其中 p + q = n-1，且p q均为非负整数。 事实上，当上述p从0取到n-1，q从n-1取到0后，所有情况就遍历完了。
        if n == 0:
            return []
        total_l = []
        total_l.append([None])
        total_l.append(["()"])
        for i in range(2, n + 1):  # 开始计算i时的括号组合，记为l
            l = []
            for j in range(i):  # 遍历所有可能的括号内外组合
                now_list1 = total_l[j]  # j + i - 1 -j = i - 1
                now_list2 = total_l[i - 1 - j]
                print(now_list1, now_list2)
                for k1 in now_list1:  # 开始具体取内外组合的实例
                    for k2 in now_list2:
                        if k1 == None:
                            k1 = ""
                        if k2 == None:
                            k2 = ""
                        el = "(" + k1 + ")" + k2
                        l.append(el)
            total_l.append(l)
        return total_l[n]

        # 2. 递归 回溯剪枝 O(2^n)
        # 局部不合法，不再递归
        # 左括号和右括号数量是固定的
        self.list = []
        self._gen(0, 0, n, "")
        return self.list

    def _gen(self, left, right, n, result):
        """
            left: 左括号用了多少个
            right：右括号用了多少个
            n： 括号对数
            result：当前产生的括号序列
        """
        # print(result)
        if left == n and right == n:
            self.list.append(result)
            return
        if left < n:  # 进入左子树条件： ( 括号小于 n
            # print(left)
            self._gen(left + 1, right, n, result + "(")  # 递归往后退时就会得到剩余情况
        if left > right and right < n:  # 进入右子树条件：）括号小于（ 括号 并且 ）括号小于 n
            # print(left, right)
            self._gen(left, right + 1, n, result + ")")