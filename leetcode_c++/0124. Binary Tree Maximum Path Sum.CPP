/*
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
    int max_sum = INT_MIN;
    int helper(TreeNode* root){
        if(nullptr == root){
            return 0;
        }
        int left = max(helper(root->left), 0);
        int right = max(helper(root->right), 0);
        int cur_val = left + right + root->val;
        max_sum = max(cur_val, max_sum);
        return root->val + max(left, right);
    }
    int maxPathSum(TreeNode* root) {
        helper(root);
        return max_sum;
    }
};


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
// class Solution {
// public:
//     int max_sum = INT_MIN;
//     int helper(TreeNode* root){
//         if(nullptr == root){
//             return 0;
//         }
//         int left = max(helper(root->left), 0);
//         int right = max(helper(root->right), 0);
//         int cur_val = left + right + root->val;
//         max_sum = max(cur_val, max_sum);
//         return root->val + max(left, right);
//     }
//     int maxPathSum(TreeNode* root) {
//         helper(root);
//         return max_sum;
//     }
// };

typedef struct _ResultType{
    int max_sum = INT_MIN;
    int path_sum = INT_MIN;
}ResultType;
class Solution {
public:
    ResultType helper(TreeNode* root){
        ResultType rt = ResultType();
        if(root == nullptr){
            return rt;
        }
        ResultType left = helper(root->left);
        ResultType right = helper(root->right);
        rt.path_sum = max(max(left.path_sum, right.path_sum),0) + root->val;
        int cur_sum = max(left.path_sum, 0) + max(right.path_sum, 0) + root->val;
        rt.max_sum = max(max(left.max_sum, right.max_sum), cur_sum);
        return rt;
    }
    int maxPathSum(TreeNode* root) {
        return helper(root).max_sum;
    }
};
