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
    int sumNumbers(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }
        return traverse(root, root->val);
    }
private:
    int traverse(TreeNode* root, int sum) {
        if (root->left == NULL && root->right == NULL) {
            return sum;
        }
        
        int res = 0;
        if (root->left != NULL) {
            res += traverse(root->left, sum * 10 + root->left->val);
        }
        if (root->right != NULL) {
            res += traverse(root->right, sum * 10 + root->right->val);
        }
        return res;
    }
};
