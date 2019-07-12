"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给定一个整数 n，返回 n 皇后不同的解决方案的数量。

示例:

输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 伪代码
def DFS(row, col, pie, na):
    if row >= n:  # 递归终止条件
        count += 1  # count是全局变量
        return
    # 列撇捺位置用或操作合在一起，取反后1是我们可以访问的位置
    # 1左移n位再减1，会使得末尾n位为为1，高位为0
    # 与了之后，就只有末位n维保留原值
    bits = (~(col|pie|na)) & ((1<<n)-1)  # 得到空位
    while bits > 0:  # 空位还没有被占光，就遍历空位
        P = bits & -bits  # 得到一个空位，得到最后的一个1，也就就是当前遍历的位置
        DFS(row + 1, col|P, (pie|P)<<1, (na|P)>>1)  # 列只需要对应位置或，撇和捺在下一层需要左移和右移
        bits &= bits -1  # 去掉将最后一个1，这一位以及被遍历，去掉


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1: return []
        self.count = 0
        self.DFS(n, 0, 0, 0, 0)
        return self.count

    def DFS(self, n, row, cols, pie, na):
        # 递归终止
        if row >= n:
            self.count += 1
            return

        bits = (~(cols | pie | na)) & ((1 << n) - 1)  # 得到当前所有的空位

        while bits:
            p = bits & -bits  # 取得最低位的1
            self.DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
            bits = bits & (bits - 1)  # 去掉最低位的1
