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
    vector<TreeNode*> generateTrees(int n) {
        vector<TreeNode *> res;
        if (n == 0) {
            return res;
        }
        dfs(1, n, res);
        return res;
    }
private:
    void dfs(int left, int right, vector<TreeNode *> &res) {
        if (left > right) {
            res.push_back(NULL);
            return;
        }
        int i, j, k;
        vector<TreeNode *> left_res, right_res;
        TreeNode *root;
        int nl, nr;
        for (i = left; i <= right; ++i) {
            dfs(left, i - 1, left_res);
            dfs(i + 1, right, right_res);
            nl = left_res.size();
            nr = right_res.size();
            for (j = 0; j < nl; ++j) {
                for (k = 0; k < nr; ++k) {
                    root = new TreeNode(i);
                    root->left = left_res[j];
                    root->right = right_res[k];
                    res.push_back(root);
                }
            }
            left_res.clear();
            right_res.clear();
        }
    }
};
