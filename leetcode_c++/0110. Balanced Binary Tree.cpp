/*
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
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
 typedef struct _ResultType {
     int depth = 0;
     bool isBalanced = false;
 }ResultType;

class Solution {
public:
    ResultType helper(TreeNode* root){
        ResultType rt = ResultType();
        if(root == NULL){
            rt.isBalanced = true;
            return rt;
        }
        ResultType left = helper(root->left);
        ResultType right = helper(root->right);
        rt.depth = max(left.depth, right.depth) + 1;
        if(!left.isBalanced || !right.isBalanced){
            rt.isBalanced = false;
            return rt;
        }
        if(abs(left.depth - right.depth) <= 1){
            rt.isBalanced = true;
        } else{
            rt.isBalanced = false;
        }
        return rt;
    }
    bool isBalanced(TreeNode* root) {
        return helper(root).isBalanced;
    }
};
