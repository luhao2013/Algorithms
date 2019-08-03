"""
输入两个递增排序的链表，合并这两个链表并使新链表中的结点仍然时按照递增排序的。
"""

class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    def append(self, next):
        self.next = next

def merge(head1, head2):
    if not head1:
        return head2
    elif not head2:
        return head1

    mergehead = None
    if head1.value < head2.value:
        mergehead = head1
        mergehead.next = merge(head1.next, head2)
    else:
        mergehead = head2
        mergehead.next = merge(head1, head2.next)
    return mergehead
