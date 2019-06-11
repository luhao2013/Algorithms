"""
冒泡排序从后依此将最大的数值排好位置
最好时间复杂度O(n), 最坏O(n^2)
冒泡排序是稳定的排序方法
"""

def bubble_sort(array):
    # swap = False
    # for i in range(len(array)):
    #     swap = True
    #     for j in range(1, len(array)-i):  # 位置0的元素自动排好
    #         if array[j-1] > array[j]:
    #             swap = False
    #             array[j-1], array[j] = array[j], array[j-1]

    # swap = False
    # while not swap:
    #     print('bubble sort:' + str(array))
    #     swap = True
    #     for i in range(1, len(array)):
    #         if array[i-1] > array[i]:
    #             swap = False
    #             array[i-1], array[i] = array[i], array[i-1]

    # 改进，记录最后交换的地方,减少比较次数使用这种改进
    swap = len(array) - 1
    while swap > 0:                                        # 最多进行n-1趟
        last = 0
        for i in range(0, swap):
            if array[i] > array[i+1]:
                last = i
                array[i], array[i+1] = array[i+1], array[i]
        swap = last


if __name__ == '__main__':
    testList = [1, 3, 5, 7, 2, 6, 25, 18, 13]

    bubble_sort(testList)
    print(testList)