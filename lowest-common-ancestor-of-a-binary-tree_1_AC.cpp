/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
// The interface of this problem is not suitable for offline algorithms.
#include <unordered_map>
using std::unordered_map;

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (p == NULL || q == NULL) {
            return NULL;
        }
        unordered_map<TreeNode *, int> depth;
        unordered_map<TreeNode *, TreeNode *> parent;
        
        depth[NULL] = NULL;
        parent[root] = NULL;
        visit(root, 1, depth, parent);
        
        while (depth[p] > depth[q]) {
            p = parent[p];
        }
        while (depth[q] > depth[p]) {
            q = parent[q];
        }
        while (p != q) {
            p = parent[p];
            q = parent[q];
        }
        depth.clear();
        parent.clear();
        return p;
    }
private:
    void visit(TreeNode *root, int d, unordered_map<TreeNode *, int> &depth,
        unordered_map<TreeNode *, TreeNode *> &parent) {
        depth[root] = d;
        if (root->left != NULL) {
            parent[root->left] = root;
            visit(root->left, d + 1, depth, parent);
        }
        if (root->right != NULL) {
            parent[root->right] = root;
            visit(root->right, d + 1, depth, parent);
        }
    }
};
