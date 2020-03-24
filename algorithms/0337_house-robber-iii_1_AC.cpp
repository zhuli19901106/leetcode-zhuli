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
    Solution() {
        local[NULL] = 0;
        global[NULL] = 0;
    }
    
    int rob(TreeNode* root) {
        traverse(root);
        return global[root];
    }
    
    ~Solution() {
        local.clear();
        global.clear();
    }
private:
    unordered_map<TreeNode*, int> local;
    unordered_map<TreeNode*, int> global;
    
    void traverse(TreeNode *root) {
        if (global.find(root) != global.end()) {
            return;
        }
        traverse(root->left);
        traverse(root->right);
        
        int res1 = global[root->left] + global[root->right];
        int res2 = root->val;
        if (root->left != NULL) {
            res2 += global[root->left->left];
            res2 += global[root->left->right];
        }
        if (root->right != NULL) {
            res2 += global[root->right->left];
            res2 += global[root->right->right];
        }
        local[root] = res2;
        global[root] = max(res1, res2);
    }
};
