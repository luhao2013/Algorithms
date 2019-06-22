"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # 1 中序遍历 左中右遍历得到一个有序数组, 复杂度较高
    def orderBST(self, root):
        # 中序遍历
        if root == None:
            return []
        return self.orderBST(root.left) + [root.val] + self.orderBST(root.right)

    # 2. 中序遍历，优化，只需要保存前继节点
    def helper(self, root):
        if root == None:
            return True
        if not self.helper(root.left):  # 中序遍历，左-->操作-->右
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root  # 自己赋值给前继节点
        return self.helper(root.right)

    # 3. 递归，将左值和右值都返回和根节点比较
    def recursive(self, root, min, max):
        if root == None:
            return True
        if min != None and root.val <= min:
            return False
        if max != None and root.val >= max:
            return False

        return self.recursive(root.left, min, root.val) and self.recursive(root.right, root.val, max)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #         # 1. 中序遍历，复杂度较高
        #         arr = self.orderBST(root)
        #         return arr == list(sorted(set(arr)))  # 用set是因为题目里显示没有重复项

        # 2. 中序遍历，优化，只需要保存前继节点
        self.prev = None
        return self.helper(root)

        # # 3. 递归，将左值和右值都返回和根节点比较
        # min = None
        # max = None
        # return self.recursive(root, min, max)
