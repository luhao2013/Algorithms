"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # a 左---》push
        # b 右---》pop，不匹配则错误
        # c stack为空

        # 将左括号压入栈，遇到右括号弹出栈看是否匹配
        stack = []
        character_map = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c not in character_map:  # 左括号入栈
                stack.append(c)
            elif not stack or character_map[c] != stack.pop():  # 直接比较pop出的优化时间
                return False
        return not stack
