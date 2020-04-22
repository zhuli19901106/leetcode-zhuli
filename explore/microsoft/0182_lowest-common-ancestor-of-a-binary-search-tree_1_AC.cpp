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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == NULL || p == NULL || q == NULL) {
            return NULL;
        }
        if (p->val > q->val) {
            return lowestCommonAncestor(root, q, p);
        }
        while (true) {
            if (root->val < p->val) {
                root = root->right;
            } else if (root->val > q->val) {
                root = root->left;
            } else {
                return root;
            }
        }
    }
};
