/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <queue>
#include <vector>
using std::queue;
using std::vector;

class Solution {
public:
    int findSecondMinimumValue(TreeNode* root) {
        if (root == NULL) {
            return -1;
        }
        
        v1 = root->val;
        v2 = -1;
        traverse(root);
        
        return v2;
    }
private:
    int v1, v2;
    
    void traverse(TreeNode *root) {
        if (root == NULL) {
            return;
        }
        
        if (v2 == -1) {
            if (root->val > v1) {
                v2 = root->val;
            }
        } else if (root->val > v1 && root->val < v2) {
            v2 = root->val;
        } else if (root->val >= v2) {
            return;
        }
        
        traverse(root->left);
        traverse(root->right);
    }
};
