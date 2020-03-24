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
    TreeNode* convertBST(TreeNode* root) {
        int sum = 0;
        traverse(root, sum);
        return root;
    }
private:
    void traverse(TreeNode *root, int &sum) {
        if (root == NULL) {
            return;
        }
        traverse(root->right, sum);
        sum = (root->val += sum);
        traverse(root->left, sum);
    }
};
