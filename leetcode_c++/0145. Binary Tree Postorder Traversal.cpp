/*
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> result;
        if(nullptr == root){
            return result;
        }
        TreeNode* prev = nullptr;
        stack<TreeNode*> s;
        s.push(root);
        while(!s.empty()){
            TreeNode* cur = s.top();
            if(nullptr == prev || prev->left == cur || prev->right == cur){
                // 从上往下走
                // 有左子树压左子树，否则压右子树，保留根节点
                if(nullptr != cur->left){
                    s.push(cur->left);
                } else if(nullptr != cur->right){
                    s.push(cur->right);
                }
            } else if(cur->left == prev){
                // 从下往上走，回退到根节点，把右子树压进去
                // 保留根节点
                if(nullptr != cur->right){
                    s.push(cur->right);
                }
            } else { // 左右都已经访问过
                result.push_back(cur->val);
                s.pop();
            }
            prev = cur;
        }
        return result;
    }
};
