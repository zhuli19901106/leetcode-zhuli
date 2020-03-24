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
    TreeNode* deleteNode(TreeNode* root, int key) {
        TreeNode *target = root;
        TreeNode *parent = NULL;
        // 0 for left, 1 for right;
        int dir = 0;
        while (target != NULL && target->val != key) {
            parent = target;
            if (key < target->val) {
                dir = 0;
                target = target->left;
            } else {
                dir = 1;
                target = target->right;
            }
        }
        if (target == NULL) {
            // Not found at all
            return root;
        }
        
        TreeNode *new_target = target;
        int new_key;
        if (target->left != NULL) {
            new_target = target->left;
            while (new_target->right != NULL) {
                new_target = new_target->right;
            }
            new_key = new_target->val;
            target->left = deleteNode(target->left, new_key);
            target->val = new_key;
        } else if (target->right != NULL) {
            new_target = target->right;
            while (new_target->left != NULL) {
                new_target = new_target->left;
            }
            new_key = new_target->val;
            target->right = deleteNode(target->right, new_key);
            target->val = new_key;
        } else {
            if (parent == NULL) {
                root = NULL;
            } else if (dir) {
                parent->right = NULL;
            } else {
                parent->left = NULL;
            }
            delete target;
        }
        return root;
    }
};
