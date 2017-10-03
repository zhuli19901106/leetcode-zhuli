/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
// Stay simple, stay naive.
class Solution {
public:
    TreeNode* trimBST(TreeNode* root, int L, int R) {
        if (root == NULL) {
            return NULL;
        }
        if (root->val < L) {
            return trimBST(root->right, L, R);
        }
        if (root->val > R) {
            return trimBST(root->left, L, R);
        }
        TreeNode *ptr = new TreeNode(root->val);
        ptr->left = trimBST(root->left, L, R);
        ptr->right = trimBST(root->right, L, R);
        
        return ptr;
    }
};
