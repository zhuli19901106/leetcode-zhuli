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
    vector<int> largestValues(TreeNode* root) {
        vector<int> res;
        traverse(root, 0, res);
        
        return res;
    }
private:
    void traverse(TreeNode *root, int depth, vector<int> &res) {
        if (root == NULL) {
            return;
        }
        
        if (res.size() <= depth) {
            res.push_back(root->val);
        } else {
            res[depth] = max(res[depth], root->val);
        }
        traverse(root->left, depth + 1, res);
        traverse(root->right, depth + 1, res);
    }
};