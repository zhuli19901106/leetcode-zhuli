// I don't think an O(logN) solution exists.
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <unordered_set>
using std::unordered_set;

class Solution {
public:
    bool findTarget(TreeNode* root, int k) {
        unordered_set<int> us;
        return traverse(root, k, us);
    }
private:
    bool traverse(TreeNode *root, int target, unordered_set<int> &us) {
        if (root == NULL) {
            return false;
        }
        if (traverse(root->left, target, us)) {
            return true;
        }
        if (us.find(target - root->val) != us.end()) {
            return true;
        } else {
            us.insert(root->val);
        }
        if (traverse(root->right, target, us)) {
            return true;
        }
        return false;
    }
};
