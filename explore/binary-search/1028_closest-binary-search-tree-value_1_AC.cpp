// Inorder traversal it is.
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <cmath>
#include <stack>
using std::fabs;
using std::stack;

class Solution {
public:
    int closestValue(TreeNode* root, double target) {
        stack<TreeNode *> st;
        TreeNode *p = root;
        int res = root->val;
        int val;
        while (true) {
            while (p != NULL) {
                st.push(p);
                p = p->left;
            }
            if (st.empty()) {
                break;
            }
            
            p = st.top()->right;
            val = st.top()->val;
            st.pop();
            
            if (fabs(val - target) < fabs(res - target)) {
                res = val;
            }
            if (val >= target) {
                break;
            }
        }
        while (!st.empty()) {
            st.pop();
        }
        return res;
    }
};
