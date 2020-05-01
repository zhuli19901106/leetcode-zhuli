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
using std::reverse;

class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> res;
        preorder(root, 0, res);
        int n = res.size();
        int i;
        for (i = 1; i < n; i += 2) {
            reverse(res[i].begin(), res[i].end());
        }
        return res;
    }
private:
    void preorder(TreeNode *root, int depth, vector<vector<int>> &res) {
        if (root == NULL) {
            return;
        }
        while (res.size() <= depth) {
            res.push_back(vector<int>());
        }
        res[depth].push_back(root->val);
        if (root->left != NULL) {
            preorder(root->left, depth + 1, res);
        }
        if (root->right != NULL) {
            preorder(root->right, depth + 1, res);
        }
    }
};
