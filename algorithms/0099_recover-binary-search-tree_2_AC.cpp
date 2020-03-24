// Is it really necessary to show off the Morris Traversal in interview?
// I don't like the looks of this.
// The idea is the same, except that this time we play smart.
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
using std::swap;

class Solution {
public:
    void recoverTree(TreeNode* root) {
        morrisInorder(root);
    }
private:
    void morrisInorder(TreeNode *root) {
        TreeNode *prev, *cur;
        TreeNode *t1, *t2;
        TreeNode *p1, *p2;

        prev = cur = NULL;
        p1 = root;
        t1 = t2 = NULL;
        while (p1 != NULL) {
            if (p1->left == NULL) {
                prev = cur;
                cur = p1;
                
                p1 = p1->right;
            } else {
                p2 = p1->left;
                while (p2->right != NULL && p2->right != p1) {
                    p2 = p2->right;
                }
                if (p2->right == NULL) {
                    p2->right = p1;
                    p1 = p1->left;
                } else {
                    p2->right = NULL;
                    
                    prev = cur;
                    cur = p1;
                    
                    p1 = p1->right;
                }
            }
            
            if (prev != NULL && prev->val > cur->val) {
                if (t1 == NULL) {
                    t1 = prev;
                }
                t2 = cur;
            }
        }
        
        if (t1 != NULL && t2 != NULL) {
            swap(t1->val, t2->val);
        }
    }
};
