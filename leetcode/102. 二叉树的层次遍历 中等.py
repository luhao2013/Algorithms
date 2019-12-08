1class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        # # 在python中，队列是用列表来模拟的，其中pop(0)的操作复杂度是O(n)
        # if root == None:
        #     return []
        # value_list = []
        # node_list = [root]
        # while node_list:
        #     value_list.append(node_list[0].val)
        #     if node_list[0].left:
        #         node_list.append(node_list[0].left)
        #     if node_list[1].right:
        #         node_list.append(node_list[1].right)
        #     node_list.pop(0)
        #
        # return value_list

        # 下面不用队列作为改进,就是一次存储一层的节点遍历，不需要pop了
        value_list = []
        current_list = [root]
        while current_list:
            next_list = []
            for i in current_list:
                value_list.append(i.val)
                if i.left:
                    next_list.append(i.left)
                if i.right:
                    next_list.append(i.right)
            current_list = next_list

        return value_list

        # 二叉树的按层输出
        value_list = []
        current_list = [root]
        while current_list:
            next_list = []
            temp_value_list = []
            for i in current_list:
                temp_value_list.append(i.val)
                if i.left:
                    next_list.append(i.left)
                if i.right:
                    next_list.append(i.right)
            current_list = next_list
            value_list.append(temp_value_list)

        return value_list