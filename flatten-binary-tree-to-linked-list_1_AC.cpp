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
    void flatten(TreeNode* root) {
        if (root == NULL) {
            return;
        }
        TreeNode *left, *right;
        traverse(root, left, right);
    }
private:
    void traverse(TreeNode *root, TreeNode *&left, TreeNode *&right) {
        TreeNode *ll, *lr, *rl, *rr;
        if (root->left != NULL) {
            traverse(root->left, ll, lr);
        } else {
            ll = lr = root;
        }
        if (root->right != NULL) {
            traverse(root->right, rl, rr);
        } else {
            rl = rr = root;
        }
        if (ll != root) {
            root->left = NULL;
            root->right = ll;
        }
        if (rr != root) {
            lr->right = rl;
        }
        left = root;
        right = (rr != root ? rr : (lr != root ? lr : root));
    }
};
