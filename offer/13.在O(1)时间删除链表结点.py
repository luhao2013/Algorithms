"""
给定单向链表的头指针和一个结点指针，定义一个函数在O(1)时间删除该结点。
"""


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def append(self, node):
        self.next = node


def DeleteNode(head, be_deleted):
    """
    O(1)时间删除结点
    :param head:单链表头指针
    :param be_deleted:要被删除的节点指针
    :return:
    """
    if not head or not be_deleted:
        return None

    # 要删除的不是尾结点
    if be_deleted.next:
        next_node = be_deleted.next
        be_deleted.value = next_node.value
        be_deleted.next = next_node.next
        del next_node
    # 链表只有一个节点，删除头节点（也是尾结点）
    elif head == be_deleted:
        del be_deleted
        be_deleted = None
        head = None
    # 链表有多个节点，删除尾结点,需要顺序遍历
    else:
        pNode = head
        while pNode.next != be_deleted:
            pNode = pNode.next
        pNode.next = None
        del be_deleted
        be_deleted = None
