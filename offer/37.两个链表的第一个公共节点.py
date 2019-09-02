"""
输入两个链表，找出它们的第一个公共结点。
"""


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        length1 = self.get_length(pHead1)
        length2 = self.get_length(pHead2)
        diff = length1 - length2

        long_list_head = pHead1
        short_list_head = pHead2
        if length2 > length1:
            long_list_head = pHead2
            short_list_head = pHead1
            diff = length2 - length1

        for _ in range(diff):
            long_list_head = long_list_head.next

        while long_list_head != short_list_head:
            short_list_head = short_list_head.next
            long_list_head = long_list_head.next

        return long_list_head

    def get_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
