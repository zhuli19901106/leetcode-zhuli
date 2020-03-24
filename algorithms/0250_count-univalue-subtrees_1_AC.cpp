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
    int countUnivalSubtrees(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }
        int cnt = 0;
        traverse(root, cnt);
        return cnt;
    }
private:
    bool traverse(TreeNode *root, int &cnt) {
        if (root->left == NULL && root->right == NULL) {
            ++cnt;
            return true;
        }
        
        bool res = true;
        if (root->left != NULL && (!traverse(root->left, cnt) || 
            root->val != root->left->val)) {
            res = false;
        }
        if (root->right != NULL && (!traverse(root->right, cnt) || 
            root->val != root->right->val)) {
            res = false;
        }
        
        if (res) {
            ++cnt;
        }
        return res;
    }
};
