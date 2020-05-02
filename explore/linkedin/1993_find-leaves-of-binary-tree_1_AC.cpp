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
#include <vector>
using std::max;
using std::vector;

class Solution {
public:
    vector<vector<int>> findLeaves(TreeNode* root) {
        vector<vector<int>> res;
        (void)traverse(root, res);
        return res;
    }
private:
    int traverse(TreeNode *root, vector<vector<int>> &res) {
        if (root == NULL) {
            return 0;
        }
        
        int d = max(traverse(root->left, res), traverse(root->right, res)) + 1;
        while (res.size() < d) {
            res.push_back(vector<int>());
        }
        res[d - 1].push_back(root->val);
        return d;
    }
};
