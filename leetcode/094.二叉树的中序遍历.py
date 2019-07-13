"""
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 解法1 递归
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        self.inOrder(root)
        return self.result

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            self.result.append(root.val)
            self.inOrder(root.right)


# 解法2 迭代
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        stack, result = [], []
        while stack or root:
            # 把左子树压入栈中
            while root:
                stack.append(root)
                root = root.left
            # 输出 栈顶元素
            root = stack.pop()
            result.append(root.val)
            # 看右子树
            root = root.right
        return result
