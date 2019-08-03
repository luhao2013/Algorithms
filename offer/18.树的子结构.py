"""
输入两颗二叉树A和B，判断B是是不是A的子结构。
"""


class BinaryTreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


# 要查找树A中是否存在和树B结构一样的子树，我们可以分为两步：
# 第一步在树A中找到和B的根节点值一样的结点R
# 第二步再判断树A中以R为根节点的子树是不是包含和树B一样的结构
# 第一步在树A中查找与根节点的值一样的结点，这实际上就是树的遍历。
# 可以用递归的方法去遍历，也可以用循环的方法去遍历

def HasSubTree(root1, root2):
    result = False

    if root1 and root2:
        if root1.value == root2.value:
            result = DoesTree1HaveTree2(root1, root2)
        if not result:
            result = HasSubTree(root1.left, root2)
        if not result:
            result = HasSubTree(root1.right, root2)
    return result

def DoesTree1HaveTree2(root1, root2):
    if not root2:
        return True
    if not root1:
        return False
    if root1.value != root2.value:
        return False
    return DoesTree1HaveTree2(root1.left, root2.left) and \
           DoesTree1HaveTree2(root1.right, root2.right)
