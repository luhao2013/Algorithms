"""
简单选择排序：每一趟找出最小的元素和前面进行交换
最好、最坏和平均的时间复杂度都为O(n^2)
"""

def selection_sort(array):
    for i in range(0, len(array)-1):
        small = i
        for j in range(i+1, len(array)):
            if array[j] < array[small]:
                small = j
        array[i], array[small] = array[small], array[i]


if __name__ == "__main__":
    testList = [1, 3, 5, 7, 2, 6, 25, 18, 13]

    selection_sort(testList)
    print(testList)