# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 解法1 集合
        has_detected = set()
        while headA and headB:
            if headA in has_detected:
                return headA
            elif headB in has_detected:
                return headB
            elif headA == headB:
                return headA
            has_detected.add(headA)
            has_detected.add(headB)
            headA = headA.next
            headB = headB.next
        if not headA:
            while headB:
                if headB in has_detected:
                    return headB
                headB = headB.next
        elif not headB:
            while headA:
                if headA in has_detected:
                    return headA
                headA = headA.next

        # 解法2， 将一个链表首尾相连，就变成了找环路中第一个节点的问题
        if not headA or not headB:
            return None

        last = headB
        while last.next:
            last = last.next
        last.next = headB

        fast = headA
        slow = headA

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = headA
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                last.next = None  # 把环路断开恢复原样
                return fast
        last.next = None  # 把环路断开恢复原样
        return None