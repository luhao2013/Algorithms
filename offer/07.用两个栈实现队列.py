"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数appendTail和deleteHead，
分别完成在队列尾部插入结点和在队列头部删除节点的功能
"""


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, element):
        self.stack1.append(element)

    def deleteHead(self):
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            if len(self.stack2) == 0:
                raise Exception('queue is empty!')
        return self.stack2.pop()
