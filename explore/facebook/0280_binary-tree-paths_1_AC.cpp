#include <string>
using std::to_string;
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
    vector<string> binaryTreePaths(TreeNode* root) {
        res.clear();
        path.clear();
        
        if (root != NULL) {
            traverse(root);
        }
        return res;
    }
private:
    vector<string> res;
    vector<TreeNode*> path;
    
    void traverse(TreeNode* root) {
        path.push_back(root);
        if (root->left == NULL && root->right == NULL) {
            string s = to_string(path[0]->val);
            int n = path.size();
            int i;
            for (i = 1; i < n; ++i) {
                s += "->" + to_string(path[i]->val);
            }
            res.push_back(s);
        } else {
            if (root->left != NULL) {
                traverse(root->left);
            }
            if (root->right != NULL) {
                traverse(root->right);
            }
        }
        path.pop_back();
    }
};
