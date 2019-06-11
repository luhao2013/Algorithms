"""
快速排序：递归的划分到不能划分为止
快排是目前最快的排序方法，适合元素多的情形，而且偏爱基本无序的序列。
若元素较少，则效率还不如前面的简单排序方法。快排是不稳定的排序方法。

最坏情况是每次分割的两个子序列种有一个为空时，即初始序列有序，效率
最低，时间复杂度为O(n^2)。
但在平均情况下，快排的时间复杂度为O(nlogn)。

快排可以用于下列场合：已知第k小关键字元素在表中的位置，要在尽可能短
的时间内，在较多的元素种找出前k个小关键字元素，且找出的元素需按非递
减排列，则可以先用第k小关键字元素作为分割元素进行一趟快速排序，再用
简单选择排序方法进行排序即可。
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