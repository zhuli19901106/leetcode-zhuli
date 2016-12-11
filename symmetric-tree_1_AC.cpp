// Recursive solution
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
    bool isSymmetric(TreeNode* root) {
        if (root == NULL) {
            return true;
        }
        return isMirror(root->left, root->right);
    }
private:
    bool isMirror(TreeNode* root1, TreeNode* root2) {
        if (root1 == NULL) {
            return root2 == NULL;
        }
        if (root2 == NULL) {
            return root1 == NULL;
        }
        return root1->val == root2->val && isMirror(root1->left, root2->right)
               && isMirror(root1->right, root2->left);
    }
};
