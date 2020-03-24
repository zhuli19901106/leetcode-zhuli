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
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> res;
        if (root == NULL) {
            return res;
        }
        vector<int> path;
        path.push_back(root->val);
        dfs(path, root, root->val, sum, res);
        path.pop_back();
        
        return res;
    }
private:
    void dfs(vector<int> &path, TreeNode *root, int sum, int target, 
             vector<vector<int>> &res) {
        if (root->left == NULL && root->right == NULL) {
            if (sum == target) {
                res.push_back(path);
            }
            return;
        }
        if (root->left != NULL) {
            path.push_back(root->left->val);
            dfs(path, root->left, sum + root->left->val, target, res);
            path.pop_back();
        }
        if (root->right != NULL) {
            path.push_back(root->right->val);
            dfs(path, root->right, sum + root->right->val, target, res);
            path.pop_back();
        }
    }
};
