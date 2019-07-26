"""
请实现一个函数，把字符串中的每个空格替换成"%20"。例如输入“We are happy.”,
则输出“We%20are%20happy.”
"""


# 普通的遍历会多次移动后面的元素，时间复杂度为O(n^2)
# 能够计算出最终的长度就可以只移动一次
# 先遍历一次字符串，这样就能统计出字符串中空格的总数，替换以后字符串的长度等于原来的
# 长度加上2乘以空格数目，时间复杂度为O(n)

def ReplaceBlank(string, maxlen):
    """
    :param string:假设是c++的char数组，结尾是'\0',后面会有空位
    :param maxlen:最大长度
    :return: 新的数组
    """
    if not string:
        return string
    length = 0  # 当前长度
    number_blank = 0  # 空格的个数
    i = 0
    while string[i] != '\0':
        length += 1
        if string[i] == ' ':
            number_blank += 1
        i += 1
    newlength = length + 2 * number_blank
    if newlength > maxlen:
        return None
    while (length >= 0) and (length < newlength):  # 前面指针还没越界，并且后指针还没有追上前指针
        if string[length] == ' ':
            string[newlength] = '0'
            newlength -= 1
            string[newlength] = '2'
            newlength -= 1
            string[newlength] = '%'
            newlength -= 1
        else:
            string[newlength] = string[length]
            newlength -= 1
        length -= 1
