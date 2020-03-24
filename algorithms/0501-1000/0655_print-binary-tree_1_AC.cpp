// Think more, code less.
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
#include <string>
#include <vector>
using std::max;
using std::string;
using std::vector;

class Solution {
public:
    vector<vector<string>> printTree(TreeNode* root) {
        vector<vector<string>> res;
        if (root == NULL) {
            return res;
        }
        max_dep = depth(root);
        max_width = (1 << max_dep) - 1;
        
        res.resize(max_dep, vector<string>(max_width, string("")));
        fill(root, 0, res, 0, max_width - 1);
        
        return res;
    }
private:
    int max_dep;
    int max_width;
    
    int depth(TreeNode *root) {
        if (root == NULL) {
            return 0;
        }
        return max(depth(root->left), depth(root->right)) + 1;
    }
    
    void fill(TreeNode *root, int dep, vector<vector<string>> &res, int ll, int rr) {
        if (root == NULL) {
            return;
        }
        int mm = ll + (rr - ll >> 1);
        res[dep][mm] = to_string(root->val);
        fill(root->left, dep + 1, res, ll, mm - 1);
        fill(root->right, dep + 1, res, mm + 1, rr);
    }
};
