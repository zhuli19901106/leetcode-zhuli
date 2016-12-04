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
    int sumOfLeftLeaves(TreeNode* root) {
        if (root == NULL || isLeave(root)) {
            return 0;
        }
        int sum = sumOfLeftLeaves(root->left) + sumOfLeftLeaves(root->right);
        if (isLeave(root->left)) {
            sum += root->left->val;
        }
        return sum;
    }
private:
    bool isLeave(TreeNode* root) {
        return root != NULL && root->left == NULL && root->right == NULL;
    }
};
