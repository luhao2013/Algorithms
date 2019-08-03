"""
定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的头结点。
"""

class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    def append(self, next):
        self.next = next


def reverseList(head):
    if not head:
        return head
    slow = None
    fast = head
    while fast:
        temp = fast.next
        # print(temp.value)
        fast.next = slow
        slow = fast
        fast = temp
    while slow:
        print(slow.value)
        slow = slow.next

node = ListNode(0)
head = node
for i in range(1, 6):
    node.append(ListNode(i))
    node = node.next
reverseList(head)