"""
输入一个字符串，输出该字符串中字符的全排列。
"""


def my_permutation(s):
    str_set = []
    ret = []  # 返回结果

    def permutation(string):
        for i in string:
            str_tem = string.replace(i, '', 1)  # 不加1会把所有相同字母都替换
            str_set.append(i)
            if len(str_tem) > 0:
                permutation(str_tem)
            else:
                ret.append(''.join(str_set))
            str_set.pop()
    permutation(s)
    return ret
print(my_permutation('aa'))