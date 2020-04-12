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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> v;
        traverse(root, v);
        return v;
    }
private:
    void traverse(TreeNode* root, vector<int> &v) {
        if (root == NULL) {
            return;
        }
        v.push_back(root->val);
        traverse(root->left, v);
        traverse(root->right, v);
    }
};
