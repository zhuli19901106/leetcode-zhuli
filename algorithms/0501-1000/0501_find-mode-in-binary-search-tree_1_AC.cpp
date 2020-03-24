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
using std::max;

class Solution {
public:
    vector<int> findMode(TreeNode* root) {
        vector<int> res;
        vector<int> in_order;
        traverse(root, in_order);
        
        int n = in_order.size();
        if (n == 0) {
            return res;
        }
        
        int i, j;
        int max_len = 0;
        i = 0;
        while (i < n) {
            j = i + 1;
            while (j < n && in_order[i] == in_order[j]) {
                ++j;
            }
            max_len = max(max_len, j - i);
            i = j;
        }
        i = 0;
        while (i < n) {
            j = i + 1;
            while (j < n && in_order[i] == in_order[j]) {
                ++j;
            }
            if (j - i == max_len) {
                res.push_back(in_order[i]);
            }
            i = j;
        }
        in_order.clear();
        
        return res;
    }
private:
    void traverse(TreeNode *root, vector<int> &in_order) {
        if (root == NULL) {
            return;
        }
        traverse(root->left, in_order);
        in_order.push_back(root->val);
        traverse(root->right, in_order);
    }
};
