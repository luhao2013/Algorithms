"""
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），
因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""


# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        self.is_visited = [False] * (rows * cols)
        return self.movingCountCore(threshold, 0, 0, rows, cols)

    def movingCountCore(self, threshold, row, col, rows, cols):
        if row < 0 or col < 0 or row >= rows or col >= cols:
            return 0
        if self.is_visited[row * cols + col]:
            return 0
        if not self.is_move(row, col, threshold):
            return 0
        self.is_visited[row * cols + col] = True
        return self.movingCountCore(threshold, row + 1, col, rows, cols) + \
               self.movingCountCore(threshold, row, col + 1, rows, cols) + \
               self.movingCountCore(threshold, row - 1, col, rows, cols) + \
               self.movingCountCore(threshold, row, col - 1, rows, cols) + 1

    def is_move(self, rows, cols, threshold):
        count = 0
        while rows:
            count += rows % 10
            rows //= 10
        while cols:
            count += cols % 10
            cols //= 10
        return False if count > threshold else True
