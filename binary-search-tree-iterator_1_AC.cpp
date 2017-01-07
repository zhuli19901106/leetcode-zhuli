// Manual inorder traversal
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <stack>
using std::stack;

class BSTIterator {
public:
    BSTIterator(TreeNode *root) {
        TreeNode *p1 = root;
        while (p1 != NULL) {
            st.push(p1);
            p1 = p1->left;
        }
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !st.empty();
    }

    /** @return the next smallest number */
    int next() {
        TreeNode *p1 = st.top();
        st.pop();
        TreeNode *p2 = p1->right;
        while (p2 != NULL) {
            st.push(p2);
            p2 = p2->left;
        }
        return p1->val;
    }
    
    ~BSTIterator() {
        while (!st.empty()) {
            st.pop();
        }
    }
private:
    stack<TreeNode *> st;
};

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */
