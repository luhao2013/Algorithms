"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之尾数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如数组
{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1.
"""


def minInorder(array, left, right):
    """
    顺序查找最小值
    :param array:输入数组
    :param left: 左索引
    :param right: 右索引
    :return: 最小值
    """
    result = array[left]
    for i in range(left+1, right+1):
        if result > array[i]:
            result= array[i]
    return result

def Min(array):
    """
    二分查找，双指针
    :param array:输入旋转数组
    :return: 返回最小值
    """
    if not array:
        raise Exception('the array is empty!')
    left = 0
    right = len(array) - 1
    index = 0
    while array[left] >= array[right]:
        if right - left == 1:
            index = right
            break
        index = left + right // 2

        # 如果下标为left，right和index指向的三个数字相等
        # 则只能顺序查找
        if array[left] == array[right] and array[left] == array[index]:
            return minInorder(array, left, right)

        if array[index] >= array[left]:
            left = index
        else:
            right = index
    return array[index]
