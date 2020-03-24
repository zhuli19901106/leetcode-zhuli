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
        depth[NULL] = 0;
        diameter[NULL] = 0;
    }
    
    int diameterOfBinaryTree(TreeNode* root) {
        if (diameter.find(root) != diameter.end()) {
            return diameter[root];
        }
        
        int d1 = diameterOfBinaryTree(root->left);
        int d2 = diameterOfBinaryTree(root->right);
        diameter[root] = max(d1, d2);
        d1 = getDepth(root->left);
        d2 = getDepth(root->right);
        diameter[root] = max(diameter[root], d1 + d2);
        
        return diameter[root];
    }
    
    ~Solution() {
        depth.clear();
        diameter.clear();
    }
private:
    unordered_map<TreeNode *, int> depth;
    unordered_map<TreeNode *, int> diameter;
    
    int getDepth(TreeNode *root) {
        if (depth.find(root) == depth.end()) {
            depth[root] = max(getDepth(root->left), getDepth(root->right)) + 1;
        }
        
        return depth[root];
    }
};
