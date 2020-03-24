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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> v;
        if (root == NULL) {
            return v;
        }
        
        stack<TreeNode*> st;
        TreeNode *p1 = root;
        while (true) {
            while (p1 != NULL) {
                st.push(p1);
                p1 = p1->left;
            }
            if (st.empty()) {
                break;
            }
            p1 = st.top();
            v.push_back(p1->val);
            st.pop();
            
            p1 = p1->right;
        }
        
        return v;
    }
};
