/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <unordered_map>
using std::unordered_map;

class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int n = inorder.size();
        int i;
        unordered_map<int, int> um;
        for (i = 0; i < n; ++i) {
            um[inorder[i]] = i;
        }
        TreeNode *root = reconstruct(preorder, inorder, 0, n - 1, 0, n - 1, um);
        um.clear();
        return root;
    }
    
    TreeNode *reconstruct(vector<int> &pre, vector<int> &in, int l1, int r1, 
        int l2, int r2, unordered_map<int, int> &um) {
        if (l1 > r1) {
            return NULL;
        }
        TreeNode *root = new TreeNode(pre[l1]);
        int root_idx = um[root->val];
        int len_left = root_idx - l2;
        int len_right = r2 - root_idx;
        root->left = reconstruct(pre, in, l1 + 1, l1 + len_left, l2, 
            root_idx - 1, um);
        root->right = reconstruct(pre, in, r1 - len_right + 1, r1, 
            root_idx + 1, r2, um);
        return root;
    }
};
