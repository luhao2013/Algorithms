/*
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        if(nullptr == root){
            return result;
        }
        stack<TreeNode*> st;
        TreeNode* cur = root;
        while(true){
            while(nullptr != cur){
                st.push(cur);
                cur = cur->left;
            }
            if(st.empty()){
                break;
            }
            cur = st.top();
            st.pop();
            result.push_back(cur->val);
            cur = cur->right;
        }
        return result;
    }
};
