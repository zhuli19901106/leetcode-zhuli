// Such intensive recursion should always be accompanied by caching.
// Otherwise a lot of repetitive computation will be executed.
#include <unordered_map>
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
    
    int pathSum(TreeNode* root, int sum) {
        unordered_map<TreeNode*, int>::const_iterator it = cache.find(root);
        if (it != cache.end()) {
            return it->second;
        }
        int res = pathSumFromRoot(root, sum);
        if (root->left != NULL) {
            res += pathSum(root->left, sum);
        }
        if (root->right != NULL) {
            res += pathSum(root->right, sum);
        }
        cache[root] == res;
        return res;
    }
    
    ~Solution() {
        cache.clear();
    }
private:
    unordered_map<TreeNode*, int> cache;
    
    int pathSumFromRoot(TreeNode* root, int sum) {
        if (root == NULL) {
            return 0;
        }
        int res = (sum == root->val ? 1 : 0);
        if (root->left != NULL) {
            res += pathSumFromRoot(root->left, sum - root->val);
        }
        if (root->right != NULL) {
            res += pathSumFromRoot(root->right, sum - root->val);
        }
        return res;
    }
};
