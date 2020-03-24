// Manual recursion
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <stack>
using std::stack;

class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode *> st;
        TreeNode *p;
        
        p = root;
        while (true) {
            while (p != NULL) {
                st.push(p);
                p = p->left != NULL ? p->left : p->right;
            }
            if (st.empty()) {
                break;
            }
            p = st.top();
            st.pop();
            res.push_back(p->val);
            if (!st.empty() && p == st.top()->left && st.top()->right != NULL) {
                p = st.top()->right;
            } else {
                p = NULL;
            }
        }
        
        return res;
    }
};
