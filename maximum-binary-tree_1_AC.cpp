// Brute-force
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <vector>
using std::vector;

class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        int n = nums.size();
        TreeNode *root;
        
        traverse(root, nums, 0, n - 1);
        return root;
    }
private:
    void traverse(TreeNode *&root, vector<int> &v, int ll, int rr) {
        if (ll > rr) {
            root = NULL;
            return;
        }
        int mm = ll;
        int i;
        for (i = ll + 1; i <= rr; ++i) {
            if (v[i] > v[mm]) {
                mm = i;
            }
        }
        root = new TreeNode(v[mm]);
        traverse(root->left, v, ll, mm - 1);
        traverse(root->right, v, mm + 1, rr);
    }
};
