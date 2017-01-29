// The next pointer itself is a means to level-order traversal.
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
        TreeLinkNode *head, *next_head;
        TreeLinkNode *p1;
        
        head = root;
        while (head != NULL) {
            next_head = NULL;
            while (head != NULL) {
                // Locate the head of next level
                if (next_head == NULL) {
                    if (head->left != NULL) {
                        next_head = head->left;
                    } else if (head->right != NULL) {
                        next_head = head->right;
                    }
                }
                
                // Set "next" pointer for the next level
                p1 = head->next;
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
                if (head->right != NULL) {
                    head->right->next = p1;
                }
                if (head->left != NULL) {
                    head->left->next = (head->right != NULL) ? head->right : p1;
                }
                
                // Level-order traversal
                head = head->next;
            }
            // Down to next level
            head = next_head;
        }
    }
};
