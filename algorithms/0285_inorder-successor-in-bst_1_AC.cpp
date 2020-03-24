/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <stack>
using std::stack;

class Solution {
public:
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        if (root == NULL || p == NULL) {
            return NULL;
        }
        
        TreeNode *q;
        if (p->right != NULL) {
            q = p->right;
            while (q->left != NULL) {
                q = q->left;
            }
            return q;
        }
        
        TreeNode *r = root;
        q = NULL;
        while (r != p) {
            if (p->val < r->val) {
                q = r;
                r = r->left;
            } else {
                r = r->right;
            }
        }
        return q;
    }
};
