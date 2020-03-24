// Inorder traversal
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
        prev = cur = NULL;
        t1 = t2 = NULL;
        inorder(root);
        if (t1 != NULL && t2 != NULL) {
            swap(t1->val, t2->val);
        }
    }
private:
    TreeNode *prev, *cur;
    TreeNode *t1, *t2;
    
    void inorder(TreeNode *root) {
        if (root == NULL) {
            return;
        }
        
        inorder(root->left);
        
        prev = cur;
        cur = root;
        if (prev != NULL && cur->val < prev->val) {
            if (t1 == NULL) {
                t1 = prev;
            }
            t2 = cur;
        }
    
        inorder(root->right);
    }
};
