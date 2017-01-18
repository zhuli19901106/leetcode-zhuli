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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int n = inorder.size();
        int i;
        unordered_map<int, int> um;
        for (i = 0; i < n; ++i) {
            um[inorder[i]] = i;
        }
        TreeNode *root = reconstruct(inorder, postorder, 0, n - 1, 0, n - 1, um);
        um.clear();
        return root;
    }
private:
    TreeNode* reconstruct(vector<int>& in, vector<int>& post, int l1, int r1, 
        int l2, int r2, unordered_map<int, int>& um) {
        if (l1 > r1) {
            return NULL;
        }
        TreeNode *root = new TreeNode(post[r2]);
        int root_idx = um[root->val];
        int len_left = root_idx - l1;
        int len_right = r1 - root_idx;
        root->left = reconstruct(in, post, l1, root_idx - 1, l2, 
            l2 + len_left - 1, um);
        root->right = reconstruct(in, post, root_idx + 1, r1, l2 + len_left, 
            r2 - 1, um);
        return root;
    }
};
