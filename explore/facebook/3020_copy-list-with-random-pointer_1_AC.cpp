// O(1) space, whimsical.
// This time I can finally solve it without any reference.
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node *copyRandomList(Node *head) {
        if (head == NULL) {
            return NULL;
        }
        
        Node *p1, *p2;
        p1 = head;
        while (p1 != NULL) {
            p2 = p1->random;
            p1->random = new Node(p1->val);
            p1->random->next = p2;
            
            p1 = p1->next;
        }
        
        p1 = head;
        while (p1 != NULL) {
            // Set random pointer
            p2 = p1->random;
            p2->random = (p2->next != NULL) ? p2->next->random : NULL;
            
            p1 = p1->next;
        }
        
        Node *new_head = head->random;
        p1 = head;
        while (p1 != NULL) {
            // Reconstruct the old list
            // Link up the new list
            p2 = p1->random;
            p1->random = p2->next;
            p2->next = (p1->next != NULL) ? p1->next->random : NULL;
            p1 = p1->next;
        }
        
        return new_head;
    }
};
