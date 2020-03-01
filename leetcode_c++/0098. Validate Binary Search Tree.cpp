/*
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
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
 // 大于左子树最大值，小于右子树最小值
typedef struct _ResultType{
    bool isValid = false;
    long minVal = LONG_MAX;
    long maxVal = LONG_MIN;
}ResultType;
class Solution {
public:
    ResultType helper(TreeNode* root){
        ResultType rt = ResultType();
        if(nullptr == root){
            rt.isValid = true;
            return rt;
        }
        ResultType left = helper(root->left);
        ResultType right = helper(root->right);
        if(!left.isValid || !right.isValid){
            return rt;
        }
        if(left.maxVal < root->val && right.minVal > root->val){
            rt.maxVal = max((long)root->val, right.maxVal);
            rt.minVal = min((long)root->val, left.minVal);
            rt.isValid = true;
            return rt;
        } else {
            rt.isValid = false;
            return rt;
        }
    }
    bool isValidBST(TreeNode* root) {
        return helper(root).isValid;
    }
};
