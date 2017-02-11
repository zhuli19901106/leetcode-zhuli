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
#include <climits>
#include <unordered_map>
#include <vector>
using std::max;
using std::unordered_map;
using std::vector;

class Solution {
public:
    vector<int> findFrequentTreeSum(TreeNode* root) {
        unordered_map<int, int> um;
        treeSum(root, um);
        int max_cnt = 0;
        
        auto it = um.begin();
        for (it = um.begin(); it != um.end(); ++it) {
            max_cnt = max(max_cnt, it->second);
        }
        
        vector<int> res;
        for (it = um.begin(); it != um.end(); ++it) {
            if (it->second == max_cnt) {
                res.push_back(it->first);
            }
        }
        um.clear();
        
        return res;
    }
private:
    int treeSum(TreeNode *root, unordered_map<int, int> &um) {
        if (root == NULL) {
            return 0;
        }
        int s1 = treeSum(root->left, um);
        int s2 = treeSum(root->right, um);
        ++um[root->val + s1 + s2];
        return root->val + s1 + s2;
    }
};
