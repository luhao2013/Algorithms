"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    visited = [(i, j)]
                    if self._dfs(i, j, board, word, 1, visited):
                        return True
        return False

    def _dfs(self, pre_i, pre_j, board, word, k, visited):
        if k == len(word):
            return True
        for (x, y) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:

            i = pre_i + x
            j = pre_j + y
            if 0 <= i < self.m and 0 <= j < self.n and (i, j) not in visited and board[i][j] == word[k]:
                visited.append((i, j))
                # print(visited, k)
                if self._dfs(i, j, board, word, k + 1, visited):
                    return True
                visited.remove((i, j))  # 回溯

        return False
