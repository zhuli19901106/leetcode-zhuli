// Cache the result.
#include <algorithm>
#include <unordered_map>
using std::max;
using std::min;
using std::unordered_map;
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
    Solution() {
        height[NULL] = 0;
        balanced[NULL] = true;
    }
    
    bool isBalanced(TreeNode* root) {
        if (balanced.find(root) != balanced.end()) {
            return balanced[root];
        }
        
        int hl = getHeight(root->left);
        int hr = getHeight(root->right);
        if (max(hl, hr) - min(hl, hr) > 1) {
            return balanced[root] = false;
        }
        
        if (!isBalanced(root->left) || !isBalanced(root->right)) {
            return balanced[root] = false;
        }
        
        return balanced[root] = true;
    }
    
    ~Solution() {
        height.clear();
        balanced.clear();
    }
private:
    unordered_map<TreeNode*, int> height;
    unordered_map<TreeNode*, bool> balanced;
    
    int getHeight(TreeNode* root) {
        if (height.find(root) != height.end()) {
            return height[root];
        }
        return height[root] = 1 + max(getHeight(root->left), 
               getHeight(root->right));
    }
};
