// A smart recursive solution
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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        if (root == NULL) {
            return res;
        }
        traverse(root, 0, res);
        return res;
    }
private:
    void traverse(TreeNode *root, int depth, vector<int> &res) {
        // Smart
        if (res.size() <= depth) {
            res.push_back(root->val);
        }
        if (root->right != NULL) {
            traverse(root->right, depth + 1, res);
        }
        if (root->left != NULL) {
            traverse(root->left, depth + 1, res);
        }
    }
};
