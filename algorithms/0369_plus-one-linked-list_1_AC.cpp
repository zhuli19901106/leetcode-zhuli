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
    ListNode* plusOne(ListNode* head) {
        ListNode *c, *p;
        
        c = NULL;
        p = head;
        while (p != NULL) {
            if (p->val < 9) {
                c = p;
            }
            p = p->next;
        }
        
        if (c == NULL) {
            c = new ListNode(0);
            c->next = head;
            head = c;
        }
        
        ++(c->val);
        p = c->next;
        while (p != NULL) {
            p->val = 0;
            p = p->next;
        }
        
        return head;
    }
};
