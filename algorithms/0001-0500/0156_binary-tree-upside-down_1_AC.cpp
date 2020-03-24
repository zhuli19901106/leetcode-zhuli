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
    TreeNode* upsideDownBinaryTree(TreeNode* root) {
        if (root == NULL) {
            return NULL;
        }
        
        TreeNode *p1, *p2;
        TreeNode *pl, *pr;
        TreeNode *next_pl, *next_pr;
        
        p1 = root;
        p2 = p1->left;
        pl = pr = NULL;
        while (true) {
            next_pl = p1->right;
            next_pr = p1;
            
            p1->left = pl;
            p1->right = pr;
            
            pl = next_pl;
            pr = next_pr;
            
            p1 = p2;
            if (p1 != NULL) {
                root = p1;
                p2 = p2->left;
            } else {
                break;
            }
        }
        return root;
    }
};
