"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 1 BFS 迭代
        if root == None:
            return []
        result = []
        node_list = [root]
        children_list = []
        while node_list:
            current_level = []
            for node in node_list:
                current_level.append(node.val)
                if node.left:
                    children_list.append(node.left)
                if node.right:
                    children_list.append(node.right)
            result.append(current_level)
            node_list = children_list
            children_list = []
        return result

        # 2.BFS 递归
        if root == None:
            return []
        val_list = [[root.val]]
        child_list = [root.left, root.right]

        # 这里也可以不用递归，用child_list是否等于0终止
        def recusive(child_list):
            temp_val = []
            temp_child = []
            for i in child_list:
                if i != None:
                    temp_val.append(i.val)
                    temp_child.append(i.left)
                    temp_child.append(i.right)
            child_list = temp_child
            if len(child_list) == 0:
                return
            else:
                val_list.append(temp_val)
                recusive(child_list)

        recusive(child_list)
        return val_list

        # 3. 也可以用深度优先搜索，先序遍历会先访问每一层最左边的元素适合这个
        # 只是要加一个标识level
        if not root:
            return []
        self.result = []
        self._dfs(root, 0)
        return self.result

    def _dfs(self, node, level):
        if not node:
            return
        if len(self.result) < level + 1:
            self.result.append([])
        self.result[level].append(nodel.val)

        self._dfs(node.left, level + 1)
        self._dfs(node.right, level + 1)
