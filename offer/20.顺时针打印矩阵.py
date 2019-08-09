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
