"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1.迭代法
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1

        head = ListNode(0)
        output = head

        while l1 and l2:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next
        head.next = l1 if l1 else l2
        return output.next


# 2.递归法
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        merge_node = None
        if l1.val < l2.val:
            merge_node = l1
            merge_node.next = self.mergeTwoLists(l1.next, l2)
        else:
            merge_node = l2
            merge_node.next = self.mergeTwoLists(l1, l2.next)
        return merge_node
