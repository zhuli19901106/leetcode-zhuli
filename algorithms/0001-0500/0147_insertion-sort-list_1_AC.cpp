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
    ListNode* insertionSortList(ListNode* head) {
        if (head == NULL) {
            return NULL;
        }
        
        ListNode *h, *t;
        h = t = head;
        head = head->next;
        t->next = NULL;
        
        ListNode *p1, *p2;
        while (head != NULL) {
            p1 = head;
            head = head->next;
            if (p1->val <= h->val) {
                p1->next = h;
                h = p1;
                continue;
            }
            if (p1->val >= t->val) {
                t->next = p1;
                t = p1;
                t->next = NULL;
                continue;
            }
            p2 = h;
            while (true) {
                if (p2->val <= p1->val && p1->val <= p2->next->val) {
                    break;
                } else {
                    p2 = p2->next;
                }
            }
            p1->next = p2->next;
            p2->next = p1;
        }
        return h;
    }
};
