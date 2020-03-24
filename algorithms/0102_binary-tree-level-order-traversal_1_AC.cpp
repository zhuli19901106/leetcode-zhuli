// Recursive solution
// Whatever traversal you use, the result never changes.
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        v.clear();
        if (root == NULL) {
            return v;
        }
        preorder(root, 0);
        return v;
    }
private:
    vector<vector<int>> v;
    
    void preorder(TreeNode* root, int depth) {
        while (v.size() <= depth) {
            v.push_back(vector<int>());
        }
        v[depth].push_back(root->val);
        if (root->left != NULL) {
            preorder(root->left, depth + 1);
        }
        if (root->right != NULL) {
            preorder(root->right, depth + 1);
        }
    }
};
