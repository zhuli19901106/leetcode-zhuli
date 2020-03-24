/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <string>
using std::string;
using std::to_string;

class Solution {
public:
    string tree2str(TreeNode* t) {
        if (t == NULL) {
            return "";
        }
        
        string res = to_string(t->val);
        if (t->right != NULL) {
            res += "(" + tree2str(t->left) + ")(" + tree2str(t->right) + ")";
        } else if (t->left != NULL) {
            res += "(" + tree2str(t->left) + ")";
        }
        return res;
    }
};
