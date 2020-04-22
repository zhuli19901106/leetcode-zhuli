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
    bool isValidBST(TreeNode* root) {
        if (root == NULL) {
            return true;
        }
        int left, right;
        return traverse(root, left, right);
    }
private:
    bool traverse(TreeNode *root, int &left, int &right) {
        int ll, lr;
        if (root->left != NULL) {
            if (!traverse(root->left, ll, lr) || lr >= root->val) {
                return false;
            }
        } else {
            ll = lr = root->val;
        }
        
        int rl, rr;
        if (root->right != NULL) {
            if (!traverse(root->right, rl, rr) || rl <= root->val) {
                return false;
            }
        } else {
            rl = rr = root->val;
        }
        
        left = ll;
        right = rr;
        return true;
    }
};
