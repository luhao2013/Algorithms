"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def construct(pre_order, in_order):
    if (not pre_order) or (not in_order):
        return None
    return construct_tree(pre_order, in_order)

def restruct_tree(pre_order, in_order):
    # 排出两种特殊情况
    if len(pre_order) == 0:
        return None
    elif len(in_order) == 1:
        return TreeNode(in_order[0])
    else:
        root = pre_order[0]
        depth = in_order.index(root)  # 找到中序遍历该值的位置

        temp = TreeNode(root)
        temp.left = restruct_tree(pre_order[1: depth + 1], in_order[: depth])
        temp.right = restruct_tree(pre_order[depth + 1:], in_order[depth + 1:])
    return temp

# 用递归的都可以用栈来改造成迭代的

