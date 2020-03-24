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
#include <unordered_map>
using std::max;
using std::unordered_map;

class Solution {
public:
    int longestUnivaluePath(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }
        if (um.find(root) != um.end()) {
            return um[root];
        }
        
        int r1 = traverse(root->left, root->val) + traverse(root->right, root->val);
        int r2 = longestUnivaluePath(root->left);
        int r3 = longestUnivaluePath(root->right);
        um[root] = max(r1, max(r2, r3));
        
        return um[root];
    }
private:
    unordered_map<TreeNode *, int> um;
    
    int traverse(TreeNode *root, int val) {
        if (root == NULL || root->val != val) {
            return 0;
        }
        return 1 + max(traverse(root->left, val), traverse(root->right, val));
    }
};
