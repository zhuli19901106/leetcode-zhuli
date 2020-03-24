// O(1) space, whimsical.
// This time I can finally solve it without any reference.
/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        if (head == NULL) {
            return NULL;
        }
        
        RandomListNode *p1, *p2;
        p1 = head;
        while (p1 != NULL) {
            p2 = p1->random;
            p1->random = new RandomListNode(p1->label);
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
        
        RandomListNode *new_head = head->random;
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
