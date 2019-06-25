"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        # print(left_depth, right_depth)

        if root.left and root.right:
            return 1 + min(left_depth, right_depth)
        else:
            return 1 + left_depth + right_depth  # left和right至少有一个为0

        # 用BFS，第一个遇到遇到的叶子节点是最小深度，最后到达叶子节点是最大深度