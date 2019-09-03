"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #         # 1.迭代
        #         cur, prev = head, None
        #         while cur:
        #             cur.next, cur, prev = prev, cur.next, cur

        #         return prev

        # 2.递归
        if head == None or head.next == None:
            return head
        p = self.reverseList(head.next)  # p一直不变，保存链尾也就是反转后的链头
        head.next.next = head  # a ---> b <--- c 现在处在b
        head.next = None
        return p
