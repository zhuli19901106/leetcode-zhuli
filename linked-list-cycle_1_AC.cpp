// Run and run.
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == NULL || head->next == NULL) {
            return false;
        }
        
        ListNode *p1 = head;
        ListNode *p2 = head->next;
        
        while (true) {
            if (p2 == NULL || p2->next == NULL) {
                // La fine.
                return false;
            }
            if (p2 == p1) {
                // Caught up.
                return true;
            }
            p1 = p1->next;
            p2 = p2->next->next;
        }
    }
};
