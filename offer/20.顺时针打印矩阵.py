"""
输入一个矩阵，按照从外向里以顺时针的顺序依此打印出每一个数字
"""

def PrintMatrixClockwisely(numbers):
    col = len(numbers)
    row = len(numbers[0])

    if not numbers or col <= 0 or row <= 0:
        return

    start = 0
    while col > start * 2 and row > start * 2:
        PrintMatrixInCircle(numbers, col, row, start)
        start += 1


def PrintMatrixInCircle(numbers, col, row, start):
    endX = col - 1 - start
    endY = row - 1 - start

    # 从左到右打印一列
    for i in range(start, endX):
        number = numbers[start][i]
        print(number)

    # 从右到左打印一列
    if start < endY:
        for i in range(start+1, endY):
            number = numbers[i][endX]
            print(number)

    # 从右到左打印一行
    if start < endX and start < endY:
        for i in range(endX-1, start-1, -1):
            number = numbers[endY][i]
            print(number)

    # 从下到上打印一列
    if start < endX and start < endY - 1:
        for i in range(endY-1, start, -1):
            number = numbers[i][start]
            print(number)


# 在牛客网的实现
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        max_row = len(matrix) - 1
        max_col = len(matrix[0]) - 1
        row = 0
        col = 0
        self.res = []
        self.core(matrix, row, col, max_row, max_col)
        return self.res

    def core(self, matrix, row, col, max_row, max_col):
        if row > max_row or col > max_col:
            return

        for c in range(col, max_col + 1):
            self.res.append(matrix[row][c])
        if row < max_row:  # 有可以打印的元素
            for r in range(row + 1, max_row + 1):
                self.res.append(matrix[r][max_col])
        if row < max_row:  # 要考虑最上面的那行，不能是同一行
            for c in range(max_col - 1, col - 1, -1):
                self.res.append(matrix[max_row][c])
        if col < max_col:  # 要考虑最右面的那一列。不能是同一列
            for r in range(max_row - 1, row, -1):
                self.res.append(matrix[r][col])
        self.core(matrix, row + 1, col + 1, max_row - 1, max_col - 1)