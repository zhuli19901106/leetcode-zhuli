// easy
// search-in-a-binary-search-tree
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
    TreeNode* searchBST(TreeNode* root, int val) {
        TreeNode* ptr = root;
        while (ptr != nullptr) {
            if (val < ptr->val) {
                ptr = ptr->left;
            } else if (val > ptr->val) {
                ptr = ptr->right;
            } else {
                return ptr;
            }
        }
        return nullptr;
    }
};
