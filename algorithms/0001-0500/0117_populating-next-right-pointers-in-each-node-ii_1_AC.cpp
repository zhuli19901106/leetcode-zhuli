// Recursive solution
/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    void connect(TreeLinkNode *root) {
        if (root == NULL) {
            return;
        }
        
        TreeLinkNode *p1 = root->next;
        while (p1 != NULL) {
            if (p1->left != NULL) {
                p1 = p1->left;
                break;
            } else if (p1->right != NULL) {
                p1 = p1->right;
                break;
            } else {
                p1 = p1->next;
            }
        }
        if (root->right != NULL) {
            root->right->next = p1;
        }
        if (root->left != NULL) {
            root->left->next = (root->right != NULL) ? root->right : p1;
        }
        connect(root->right);
        connect(root->left);
    }
};
