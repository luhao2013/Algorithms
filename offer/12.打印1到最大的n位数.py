"""
输入数字n，按顺序打印出从1最大的n位十进制数。比如输入3，则打印出1、2、3一直到最大的三位数即999。
"""


# 常规的解法会遇到数值溢出问题
# 在字符串熵模拟数字加法的解法，绕过陷阱才能拿到offer
def Print1ToMaxOfNDigits(n):
    if n <= 0:
        return None
    number = [0] * n

    while not Increment(number):
        print(number)
        PrintNumber(number)

# 加1时第一个字符产生了进位，则已经时最大的n位数，返回True
def Increment(number):
    print(number)
    isOverflow = False
    nTakeOver = 0
    length = len(number)
    for i in range(length, -1):  # 从最低位开始
        nSum = number[i] - '0' + nTakeOver
        if i == length:  # 加上1
            nSum += 1
        if nSum >= 10:
            if i == 0:
                isOverflow = True
            else:
                nSum -= 10
                nTakeOver = 1
                number[i] = '0' + nSum
        else:
            number[i] = '0' + nSum
            break
    return isOverflow

# 打印的时候把前面的0不打印
def PrintNumber(number):
    isBegining0 = True
    length = len(number)

    for i in range(0, length):
        if isBegining0 and number[i] != 0:
            isBegining0 = False

        if not isBegining0:
            print(number[i], end='')
Print1ToMaxOfNDigits(3)


# 把问题转换成数字排列的解法，递归让代码更简洁
# 用递归把n位数字全排列就行了
def Print1ToMaxOfNDigits(n):
    if n <= 0:
        return None
    number = [0] * n
    for i in range(10):
        number[0] = i + '0'
        Print1ToMaxOfNDigitsRecursively(number, n, 0)

def Print1ToMaxOfNDigitsRecursively(number, length, index):
    if index == length - 1:  # 递归终止条件
        PrintNumber(number)
        return None
    for i in range(10):
        number[index+1] = i + '0'
        Print1ToMaxOfNDigitsRecursively(number, length, index+1)
