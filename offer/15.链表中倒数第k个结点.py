"""
输入一个链表，输出该链表中倒数第k个结点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾结点
使倒数第1个结点。例如一个链表有6个结点，从头结点开始它们的值依此是1、2、3、4、5、6，这个链表的倒数
第3个结点是值为4的结点。
"""


class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next - None
    def append(self, next):
        self.next = next


def FindKthToTail(head, k)
    """
    寻找链表倒数第k个结点
    :param head: 链表头指针
    :param k: 无符号整数
    :return: 倒数第k个结点
    """
    # head不为空指针，k不为0
    if not head or not k:
        return None

    fast = head
    for i in range(k-1):
        if fast.next:
            fast = fast.next
        else:
            return None  # 链表长度没有k

    slow = head
    while fast.next:
        fast = fast.next
        slow = slow.next
    return slow
