// If the three is constantly modified, the statistics should be cached.
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
    Solution() {
        um[NULL] = 0;
    }
    
    int kthSmallest(TreeNode* root, int k) {
        if (root == NULL) {
            return NULL;
        }
        TreeNode *ptr = root;
        int cnt;
        
        while (true) {
            cnt = nodeCount(ptr->left);
            if (cnt < k - 1) {
                ptr = ptr->right;
                k -= cnt + 1;
            } else if (cnt > k - 1) {
                ptr = ptr->left;
            } else {
                return ptr->val;
            }
        }
    }
    
    ~Solution() {
        um.clear();
    }
private:
    unordered_map<TreeNode*, int> um;
    
    int nodeCount(TreeNode* root) {
        if (um.find(root) == um.end()) {
            um[root] = 1 + nodeCount(root->left) + nodeCount(root->right);
        }
        return um[root];
    }
};
