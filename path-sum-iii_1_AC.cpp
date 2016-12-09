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
    int pathSum(TreeNode* root, int sum) {
        if (root == NULL) {
            return 0;
        }
        int res = pathSumFromRoot(root, sum);
        if (root->left != NULL) {
            res += pathSum(root->left, sum);
        }
        if (root->right != NULL) {
            res += pathSum(root->right, sum);
        }
        return res;
    }
private:
    int pathSumFromRoot(TreeNode* root, int sum) {
        if (root == NULL) {
            return 0;
        }
        int res = (sum == root->val ? 1 : 0);
        if (root->left != NULL) {
            res += pathSumFromRoot(root->left, sum - root->val);
        }
        if (root->right != NULL) {
            res += pathSumFromRoot(root->right, sum - root->val);
        }
        return res;
    }
};
