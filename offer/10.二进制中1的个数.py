"""
请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。
例如把9表示成二进制是1001，有2位是1.因此如果输入9，该函数
输出2.
"""


# 解法1：常规解法
# 首先把n和1做与运算，判断n的最低位是不是1，接着把1左移一位得到2，再和n做与运算。
# 接着把1左移一位得到2，在和n做与运算，这样反复左移
def numberof1(n):
    count = 0
    flag = 1
    while flag:
        if n & flag:
            count +=1
        flag = (flag << 1) & 0xffffffff
    return count

# 解法2： n & n-1,最右边1会变为0
# 一个整数减去1，都是把最右边的1变成0，如果它的右边还有0，都变成1
# 它左边的位不变，这样n和n-1与运算，相当于把最右边的1变为0
def number_of_1(n):
    count = 0
    while n & 0xffffffff:  # python不会溢出，所以把大于32为的都置为0
        count += 1
        n = n & (n-1)
    return count
