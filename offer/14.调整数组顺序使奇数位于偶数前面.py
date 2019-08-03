"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，
所有偶数位于数组的后半部分。
"""


# 维护两个指针，第一个指针初始化时指向数组的第一个数字，它只向后移动；
# 第二个市镇初始化时指向数组的最后一个数字，只向前移动。在两个指针相遇之前，第一个指针总是位于第二个指针的前面。
# 如果第一个指针指向的数字是偶数，并且第二个指针指向的数字是奇数，我们就交换这两个数字
def RecorderOddEven(array):
    length = len(array)
    left = 0
    right = len(array) - 1
    while left < right:
        while array[left] % 2 == 1 and left < length:
            left += 1
        while array[right] % 2 == 0 and right >= 0:
            right -= 1
        if left < right:
            array[left], array[right] = array[right], array[left]


array = [2,4,6,1,6,7,9]
RecorderOddEven(array)
print(array)
