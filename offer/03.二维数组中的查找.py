"""
在一个二维数组中，每一行都按照从左到右递增的顺序排列，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数
"""


# 解题思路：从右上角看，小于它的数都在左边，大于它的数都在它的下边，根据一个判断分支就可决定走向
# 如果从左上角开始，它的右边和下边都大于它，无法判断走向

def Find(array, number):
    """
    :param array: 二维数组
    :param number: 待寻找的值
    :return: 返回是否找到
    """
    found = False
    if not array:
        return found
    row = 0
    column = len(array[0]) - 1
    while row<len(array) and column >=0:
        if array[row][column] == number:
            found = True
        elif array[row][column] < number:
            row += 1
        else:
            column -= 1
    return found
