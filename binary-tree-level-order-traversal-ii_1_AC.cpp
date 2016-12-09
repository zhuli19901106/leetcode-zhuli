#include <algorithm>
using std::reverse;
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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        res.clear();
        if (root == NULL) {
            return res;
        }
        levelOrder(root, 0);
        reverse(res.begin(), res.end());
        return res;
    }
private:
    vector<vector<int>> res;
    
    void levelOrder(TreeNode* root, int level) {
        if (res.size() <= level) {
            res.push_back(vector<int>());
        }
        res[level].push_back(root->val);
        if (root->left != NULL) {
            levelOrder(root->left, level + 1);
        }
        if (root->right != NULL) {
            levelOrder(root->right, level + 1);
        }
    }
};
