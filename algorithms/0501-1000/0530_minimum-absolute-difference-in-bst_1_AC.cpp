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
#include <climits>
#include <stack>
using std::min;
using std::stack;

class Solution {
public:
    int getMinimumDifference(TreeNode* root) {
        stack<TreeNode *> st;
        TreeNode *p = root;
        TreeNode *prev = NULL;
        int res = INT_MAX;
        while (true) {
            while (p != NULL) {
                st.push(p);
                p = p->left;
            }
            if (st.empty()) {
                break;
            }
            if (prev != NULL) {
                res = min(res, st.top()->val - prev->val);
            }
            prev = st.top();
            p = prev->right;
            st.pop();
        }
        return res;
    }
};
