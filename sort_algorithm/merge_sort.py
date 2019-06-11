"""
归并排序：将n个元素的序列看成是n个长度为1的有序子序列，然后两两合并子序列。
时间复杂度是O(nlogn), 辅助空间复杂度为O(n)
归并排序是一种稳定的排序方法
"""


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])

    print('merge: ' + str(left) + '&' + str(right) + ' to ' +str(result))
    return result

def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        middle = len(array) // 2
        left_array = merge_sort(array[:middle])
        right_array = merge_sort(array[middle:])
        return merge(left_array, right_array)


if __name__ == "__main__":
    testList = [1, 3, 5, 7, 2, 6, 25, 18, 13]

    # print(quick_sort(testList))
    print(merge_sort(testList))