"""
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""


# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return pHead
        self.cloneNodes(pHead)  # 第一步插入节点
        self.connectNodes(pHead)  # 第二步连接特殊指针
        return self.reconnectNode(pHead)  # 第三步拆分

    def cloneNodes(self, pHead):
        node = pHead
        while node:
            temp = RandomListNode(node.label)
            temp.next = node.next
            node.next = temp
            node = temp.next
        return pHead

    def connectNodes(self, pHead):
        node = pHead
        while node:
            next_node = node.next
            if node.random:
                next_node.random = node.random.next
            node = next_node.next
        return pHead

    def reconnectNode(self, pHead):
        node = pHead
        cloneHead = None
        cloneNode = None

        if node:
            cloneHead = cloneNode = node.next
            node.next = cloneNode.next
            node = node.next
        while node:
            cloneNode.next = node.next
            cloneNode = cloneNode.next
            node.next = cloneNode.next
            node = node.next
        return cloneHead
