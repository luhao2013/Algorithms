"""
实现函数double Power(double base, int exponentt).
求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。
"""


# 二分法的思路，32次方=16次方*16次方，依此递归
# a^n = a^{n/2} * a^{n/2}, n为偶数
#     = a^{(n-1)/2} * a^{(n-1)/2} * a, n为奇数


def equal(num1, num2):
    if (num1-num2) > -0.000001 and (num1-num2) < 0.000001:
        return True
    else:
        return False

def Power(base, exponent):
    # 对0求倒数会出错
    if equal(base, 0.0) and exponent < 0:
        return None
    if exponent < 0:
        unsign_exponent = - exponent

    result = PowerWithUnsignedExponent(base, unsign_exponent)
    if exponent < 0:
        result = 1.0 / result

    return result

def PowerWithUnsignedExponent(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base

    result = PowerWithUnsignedExponent(base, exponent >> 1)
    result *= result
    if (exponent & 0x1) == 1:
        result *= base
    return result
