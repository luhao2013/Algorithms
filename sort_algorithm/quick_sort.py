"""
快速排序：递归的划分到不能划分为止
"""


def partition(array, left, right):
    value = array[left]

    while left < right:
        while left < right and array[right] >= value:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= value:
            left += 1
        array[right] = array[left]

    array[left] = value  # 最后left的值还没复制，所以将pivot对应的value赋值

    return left


def quick_sort(array, left, right):

    # # 1. 简单实现
    # if len(array) <= 1:
    #     return array
    # pivot = array[len(array) // 2]
    # left = [x for x in array if x < pivot]
    # middle = [x for x in array if x == pivot]
    # right = [x for x in array if x > pivot]
    #
    # return quick_sort(left) + middle + quick_sort(right)

    # 2. 优化实现
    if left < right:
        pivot = partition(array, left, right)  # pivot是分组值索引
        quick_sort(array, left, pivot-1)
        quick_sort(array, pivot+1, right)


if __name__ == "__main__":
    testList = [1, 3, 5, 7, 2, 6, 25, 18, 13]

    # print(quick_sort(testList))
    quick_sort(testList, 0, len(testList)-1)
    print(testList)