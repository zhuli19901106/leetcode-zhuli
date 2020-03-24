// Manual recursion
#include <stack>
using std::stack;
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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> v;
        stack<TreeNode*> st;
        TreeNode *p1;
        
        p1 = root;
        while (true) {
            while (p1 != NULL) {
                v.push_back(p1->val);
                st.push(p1);
                p1 = p1->left;
            }
            if (st.empty()) {
                break;
            }
            p1 = st.top()->right;
            st.pop();
        }
        return v;
    }
};
