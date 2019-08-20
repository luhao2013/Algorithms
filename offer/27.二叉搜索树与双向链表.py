"""
将二叉搜索树转化成一个排序的双向链表，只调整树中结点的指向
中序遍历，根结点的left指向左子树的最后一个(最大)值，right指向右子树的(最小)值
"""


class Solution(object):
    def convert(self, tree):
        """结点转换"""
        if not tree:
            return None
        p_last = self.convert_nodes(tree, None)
        while p_last and p_last.left:  # 获取链表头结点
            p_last = p_last.left
        return p_last

    def convert_nodes(self, tree, last):
        if not tree:
            return None
        # 中序遍历，只要记录住上一个结点，然后就可以用指针把两个节点连起来了。
        if tree.left:
            last = self.convert_nodes(tree.left, last)
        if last:
            last.right = tree  # 左子树的最大值的右指针指向根节点，或根节点的右指针连上右子树的最小值
        tree.left = last  # 根节点的左指针指向左子树的最大值，或右子树最小值的左指针连上根节点
        last = tree  # 当前节点成为新的上一个结点
        if tree.right:
            last = self.convert_nodes(tree.right, last)
        return last
