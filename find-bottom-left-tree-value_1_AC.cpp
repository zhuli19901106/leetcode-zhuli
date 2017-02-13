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
    int findBottomLeftValue(TreeNode* root) {
        TreeNode *res = NULL;
        int max_depth = 0;
        traverse(root, 1, res, max_depth);
        
        return res->val;
    }
private:
    void traverse(TreeNode *root, int depth, TreeNode *&res, int& max_depth) {
        if (root == NULL) {
            return;
        }
        if (depth > max_depth) {
            res = root;
            max_depth = depth;
        }
        traverse(root->left, depth + 1, res, max_depth);
        traverse(root->right, depth + 1, res, max_depth);
    }
};
