// I suppose every node of the new tree should be newly allocated, otherwise things sure can be pretty messed up around here.
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
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        TreeNode *root = NULL;
        if (t1 == NULL && t2 == NULL) {
            return root;
        }
        
        int v1 = (t1 != NULL ? t1->val : 0);
        int v2 = (t2 != NULL ? t2->val : 0);
        root = new TreeNode(v1 + v2);
        
        TreeNode *p1, *p2;

        p1 = (t1 != NULL ? t1->left : NULL);
        p2 = (t2 != NULL ? t2->left : NULL);
        root->left = mergeTrees(p1, p2);
        
        p1 = (t1 != NULL ? t1->right : NULL);
        p2 = (t2 != NULL ? t2->right : NULL);
        root->right = mergeTrees(p1, p2);
        
        return root;
    }
};
