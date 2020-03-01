/*
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(nullptr == root || root == p || root == q){
            return root;
        }
        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);
        if(nullptr == left){
            return right;
        } else if(nullptr == right){
            return left;
        } else {
            return root;
        }
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
//     TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
//         if(nullptr == root || root == p || root == q){
//             return root;
//         }
//         TreeNode* left = lowestCommonAncestor(root->left, p, q);
//         TreeNode* right = lowestCommonAncestor(root->right, p, q);
//         if(nullptr == left){
//             return right;
//         } else if(nullptr == right){
//             return left;
//         } else {
//             return root;
//         }
//     }
// };

typedef struct _ResultType {
    bool hasp = false;
    bool hasq= false;
    TreeNode* lca = nullptr;
}ResultType;
class Solution {
public:
    ResultType helper(TreeNode* root, TreeNode* p, TreeNode* q){
        ResultType rt = ResultType();
        if(nullptr == root){
            return rt;
        }
        ResultType left = helper(root->left, p, q);
        ResultType right = helper(root->right, p, q);
        if(nullptr != left.lca){
            rt.lca = left.lca;
            return rt;
        }
        if(nullptr != right.lca){
            rt.lca = right.lca;
            return rt;
        }
        rt.hasp = root == p || left.hasp || right.hasp;
        rt.hasq = root == q || left.hasq || right.hasq;
        if(rt.hasp && rt.hasq){
            rt.lca = root;
        }
        return rt;
    }
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        return helper(root, p, q).lca;
    }
};
