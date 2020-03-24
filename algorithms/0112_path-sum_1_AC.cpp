// You can always cache the result if you like.
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
    bool hasPathSum(TreeNode* root, int sum) {
        if (root == NULL) {
            return false;
        }
        return hasPath(root, sum);
    }
private:
    bool hasPath(TreeNode* root, int sum) {
        if (root->left == NULL && root->right == NULL) {
            return root->val == sum;
        }
        bool res = false;
        if (root->left != NULL) {
            res = res || hasPath(root->left, sum - root->val);
        }
        if (root->right != NULL) {
            res = res || hasPath(root->right, sum - root->val);
        }
        return res;
    }
};
