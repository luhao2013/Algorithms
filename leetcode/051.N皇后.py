"""
给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 解法形式1
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = [0] * n
        self.nqueens(0, n, self.result)

    def nqueens(self, row, n, result):
        for col in range(0, n):  # 在该行遍历每一列
            if self.place(row, col, result):  # 判断是否满足约束函数
                result[row] = col
                if row == n-1:
                    print(self._generate_result(n))
                else:  # 不是最后一行，进入下一行
                    self.nqueens(row+1, n, result)

    def place(self, current_row, current_col, result):
        for row in range(0, current_row):
            if (result[row] == current_col) or (abs(row - current_row) == abs(result[row] - current_col)):
                return False
        return True

    # 产生leetcode要求输出格式
    def _generate_result(self, n):
        board = []
        for i in self.result:
            board.append("." * i + "Q" + "." * (n - i - 1))

        return [board[i: i + n] for i in range(0, len(board), n)]

# 解法形式2
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # 按照左上角为原点，一旦确定一行一个皇后的位置，那么它的列的值、撇的值和捺的值都定了
        # 所以只需要这三个位置的值记到集合里做为flag就好
        if n < 1:
            return []
        self.result = []
        self.cols = set()
        self.pie = set()  # 撇
        self.na = set()  # 捺
        self.DFS(n, 0, [])
        return self._generate_result(n)

    def DFS(self, n, row, cur_state):
        if row >= n:  # 行数遍历完
            self.result.append(cur_state)
            return

        # 遍历所有的列
        for col in range(n):
            # 以左上角为原点，撇方向元素元素行列和为定值，捺方向元素行列行-列为定值
            if col in self.cols or row + col in self.pie or row - col in self.na:
                # 这个位置被占用了，就continue
                continue

            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)

            self.DFS(n, row + 1, cur_state + [col])

            # 恢复现场，看一行中其它列位置是否也有方案
            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)

    # 产生leetcode要求输出格式
    def _generate_result(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append("." * i + "Q" + "." * (n - i - 1))

        return [board[i: i + n] for i in range(0, len(board), n)]


s = Solution()
s.solveNQueens(4)