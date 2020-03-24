// Trivial
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
        vector<int> res;
        traverse(root, res);
        return res;
    }
private:
    void traverse(TreeNode *root, vector<int> &res) {
        if (root == NULL) {
            return;
        }
        traverse(root->left, res);
        traverse(root->right, res);
        res.push_back(root->val);
    }
};
