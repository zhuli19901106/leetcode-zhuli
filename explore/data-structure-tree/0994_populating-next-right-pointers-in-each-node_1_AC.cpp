// I think this is magic.
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
        
        Node* p1;
        Node* p2;
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
        return root;
    }
};
