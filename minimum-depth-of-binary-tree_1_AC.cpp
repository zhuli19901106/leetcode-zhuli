// Don't take nothing for granted, even hashing or caching.
#include <algorithm>
#include <climits>
using std::min;
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
    int minDepth(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }
        return findDepth(root);
    }
private:
    int findDepth(TreeNode* root) {
        if (root->left == NULL && root->right == NULL) {
            return 1;
        }
        int res = INT_MAX;
        if (root->left != NULL) {
            res = min(res, 1 + findDepth(root->left));
        }
        if (root->right != NULL) {
            res = min(res, 1 + findDepth(root->right));
        }
        return res;
    }
};
