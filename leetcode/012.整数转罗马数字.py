"""
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

示例 1:

输入: 3
输出: "III"
示例 2:

输入: 4
输出: "IV"
示例 3:

输入: 9
输出: "IX"
示例 4:

输入: 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.
示例 5:

输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-to-roman
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict_num = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        res = ''
        carry = 1
        while num:
            temp = num % 10
            if not temp:
                pass
            elif temp < 4:
                res = dict_num[carry] * temp + res
            elif temp == 4:
                res = dict_num[carry] + dict_num[carry * 5] + res
            elif temp < 9:
                res = dict_num[carry * 5] + dict_num[carry] * (temp - 5) + res
            else:
                res = dict_num[carry] + dict_num[carry * 10] + res
            num //= 10
            carry *= 10
        return res

        # 2.贪心
        # 在以前还使用现金购物的年代，如果我们不想让对方找钱，付款的时候我们会尽量拿面值大的纸币给对方，
        # 这样才会使得我们给对方的纸币张数最少，对方点钱的时候（因为对方要检验你给的钱对不对）也最方便。
        # 最极端的一种情况，你要是都拿零钱去买一个比较贵重的东西，我相信没有人是很高兴收到你的钱的，因为他们点钱费劲。
        # 于是，“将整数转换为阿拉伯数字”的过程，就是我们用上面这张表中右边的数字作为“加法因子”去分解
        # 一个整数，并且分解的整数个数越少越好，即尽量使用靠前的数字，这可以认为是一种贪心法则。

        # 把阿拉伯数字与罗马数字可能出现的所有情况和对应关系，放在两个数组中
        # 并且按照阿拉伯数字的大小降序排列，这是贪心选择思想
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        index = 0
        res = ''
        while index < 13:
            # 注意：这里是等于号，表示尽量使用大的"面值"。一个数量级
            while num >= nums[index]:
                res += romans[index]
                num -= nums[index]
            index += 1
        return res
