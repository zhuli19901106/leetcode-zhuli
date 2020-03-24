#include <algorithm>
#include <unordered_map>
using std::max;
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
        cache[NULL] = 0;
    }
    
    int maxDepth(TreeNode* root) {
        if (cache.find(root) != cache.end()) {
            return cache[root];
        }
        return max(maxDepth(root->left), maxDepth(root->right)) + 1;
    }
    
    ~Solution() {
        cache.clear();
    }
private:
    // Caching results is a good habit.
    unordered_map<TreeNode*, int> cache;
};
