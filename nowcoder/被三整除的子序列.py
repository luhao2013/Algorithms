"""
链接：https://ac.nowcoder.com/acm/problem/21302
来源：牛客网

题目描述
给你一个长度为50的数字串,问你有多少个子序列构成的数字可以被3整除
答案对1e9+7取模
输入描述:
输入一个字符串，由数字构成，长度小于等于50
输出描述:
输出一个整数
示例1
输入
复制
132
输出
复制
3
示例2
输入
复制
9
输出
复制
1
示例3
输入
复制
333
输出
复制
7
示例4
输入
复制
123456
输出
复制
23
示例5
输入
复制
00
输出
复制
3
备注:
n为长度
子任务1: n <= 5
子任务2: n <= 20
子任务3: 无限制
"""

# https://blog.csdn.net/weixin_43922043/article/details/89164552
char = input()
dp = [[0 for _ in range(3)] for _ in range(len(char) + 1)]
Max = 1e9 + 7
for index in range(1, len(char) + 1):
    if int(char[index - 1]) % 3 == 0:
        dp[index][0] = (dp[index - 1][0] + dp[index - 1][0] + 1) % Max
        dp[index][1] = (dp[index - 1][1] + dp[index - 1][1]) % Max
        dp[index][2] = (dp[index - 1][2] + dp[index - 1][2]) % Max
    elif int(char[index - 1]) % 3 == 1:
        dp[index][0] = (dp[index - 1][0] + dp[index - 1][2]) % Max
        dp[index][1] = (dp[index - 1][1] + dp[index - 1][0] + 1) % Max
        dp[index][2] = (dp[index - 1][2] + dp[index - 1][1]) % Max
    else:
        dp[index][0] = (dp[index - 1][0] + dp[index - 1][1]) % Max
        dp[index][1] = (dp[index - 1][1] + dp[index - 1][2]) % Max
        dp[index][2] = (dp[index - 1][2] + dp[index - 1][0] + 1) % Max
print(int(dp[-1][0]))
