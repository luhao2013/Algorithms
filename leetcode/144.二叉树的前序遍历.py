"""
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 解法1 递归实现
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        self.preOrder(root)
        return self.result

    def preOrder(self, root):
        if root:
            self.result.append(root.val)
            self.preOrder(root.left)
            self.preOrder(root.right)


# 解法2 迭代实现 需要堆栈辅助实现 深度优先搜索(DFS)
# 从根节点开始，每次迭代弹出当前栈顶元素，并将其孩子节点压入栈中，先压右孩子再压左孩子。
# 在这个算法中，输出到最终结果的顺序按照 Top->Bottom 和 Left->Right，符合前序遍历的顺序。
# 时间复杂度：访问每个节点恰好一次，时间复杂度为 O(N)O(N) ，其中 NN 是节点的个数，也就是树的大小。
# 空间复杂度：取决于树的结构，最坏情况存储整棵树，因此空间复杂度是 O(N)O(N)。

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack, result = [root, ], []
        while stack:
            root = stack.pop()
            result.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)


# 解法3 莫里斯遍历
# 方法基于莫里斯的文章，可以优化空间复杂度。算法不会使用额外空间，只需要保存最终的输出结果。如果实时输出结果，
# 那么空间复杂度是 O(1)。
# 算法的思路是从当前节点向下访问先序遍历的前驱节点，每个前驱节点都恰好被访问两次。
# 首先从当前节点开始，向左孩子走一步然后沿着右孩子一直向下访问，直到到达一个叶子节点（当前节点的中序遍历前驱节点），
# 所以我们更新输出并建立一条伪边 predecessor.right = root 更新这个前驱的下一个点。如果我们第二次访问到前驱节点，
# 由于已经指向了当前节点，我们移除伪边并移动到下一个顶点。
# 如果第一步向左的移动不存在，就直接更新输出并向右移动。

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node, output = root, []
        while node:
            if not node.left:
                output.append(node.val)
                node = node.right
            else:
                predecessor = node.left

                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right

                if not predecessor.right:
                    output.append(node.val)
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    node = node.right

        return output
