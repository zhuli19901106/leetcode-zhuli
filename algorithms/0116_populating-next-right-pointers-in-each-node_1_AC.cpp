// I think this is magic.
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
        
        TreeLinkNode *p1;
        TreeLinkNode *p2;
        p1 = root;
        while (p1->left != NULL) {
            p2 = p1;
            while (p2 != NULL) {
                p2->left->next = p2->right;
                if (p2->next != NULL) {
                    p2->right->next = p2->next->left;
                }
                p2 = p2->next;
            }
            p1 = p1->left;
        }
    }
};
