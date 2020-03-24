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
    int countNodes(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }
        
        int dl = 0;
        TreeNode *p = root;
        while (p != NULL) {
            p = p->left;
            ++dl;
        }
        int dr = 0;
        p = root;
        while (p != NULL) {
            p = p->right;
            ++dr;
        }
        
        if (dl == dr) {
            return (1 << dl) - 1;
        }
        
        int ll = 0;
        int rr = (1 << dr) - 1;
        int mm;
        int i;
        while (rr - ll > 1) {
            mm = ll + (rr - ll >> 1);
            p = root;
            for (i = dr - 1; i >= 0; --i) {
                if ((mm >> i) & 1) {
                    p = p->right;
                } else {
                    p = p->left;
                }
            }
            if (p != NULL) {
                ll = mm;
            } else {
                rr = mm;
            }
        }
        return (1 << dr) - 1 + rr;
    }
};
