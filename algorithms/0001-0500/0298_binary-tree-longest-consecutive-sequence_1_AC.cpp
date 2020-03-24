/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <algorithm>
using std::max;

class Solution {
public:
    int longestConsecutive(TreeNode* root) {
        int res = 0;
        (void)traverse(root, res);
        
        return res;
    }
private:
    int traverse(TreeNode *root, int &res) {
        if (root == NULL) {
            return 0;
        }
        
        int c = 1;
        int c1 = traverse(root->left, res);
        if (root->left != NULL && root->left->val == root->val + 1) {
            c = max(c, c1 + 1);
        }
        int c2 = traverse(root->right, res);
        if (root->right != NULL && root->right->val == root->val + 1) {
            c = max(c, c2 + 1);
        }
        res = max(res, c);
        
        return c;
    }
};
