"""
插入排序：前面的k个元素保持有序，将后面的元素插入
最好情况时间复杂度O(n)
平均和最差时间复杂度O(n^2)
"""


def insert_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        print(array)
        for j in range(i-1, -1, -1):
            if array[j] < temp:
                array[j+1] = array[j]   # 元素向后移一位
            else:
                array[j+1] = temp       # 上一个元素插入目标元素
                break


if __name__ == "__main__":
    testList = [1, 3, 5, 7, 2, 6, 25, 18, 13]

    insert_sort(testList)
    print(testList)

