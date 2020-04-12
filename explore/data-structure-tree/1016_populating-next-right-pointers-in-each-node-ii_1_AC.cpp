// Recursive solution
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/
class Solution {
public:
    Node* connect(Node* root) {
        if (root == NULL) {
            return root;
        }
        
        Node *p1 = root->next;
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
        return root;
    }
};
