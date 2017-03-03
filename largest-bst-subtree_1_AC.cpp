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
    int largestBSTSubtree(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }
        
        int res = 0;
        int c;
        TreeNode *left, *right;
        (void)isBST(root, c, res, left, right);
        
        return res;
    }
private:
    bool isBST(TreeNode *root, int &c, int &res, TreeNode *&left, TreeNode *&right) {
        if (root->left == NULL && root->right == NULL) {
            c = 1;
            left = right = root;
            res = max(res, c);
            return true;
        }
        
        TreeNode *ll, *lr;
        bool bl;
        int cl;
        if (root->left != NULL) {
            bl = isBST(root->left, cl, res, ll, lr);
            if (bl && (lr->val >= root->val)) {
                bl = false;
            }
        } else {
            bl = true;
            cl = 0;
            ll = lr = root;
        }
        
        TreeNode *rl, *rr;
        bool br;
        int cr;
        if (root->right != NULL) {
            br = isBST(root->right, cr, res, rl, rr);
            if (br && (rl->val <= root->val)) {
                br = false;
            }
        } else {
            br = true;
            cr = 0;
            rl = rr = root;
        }
        
        c = cl + 1 + cr;
        left = ll;
        right = rr;
        if (bl && br) {
            res = max(res, c);
        }
        return bl && br;
    }
};
