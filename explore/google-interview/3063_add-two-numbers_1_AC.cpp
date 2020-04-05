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
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        static const int R = 10;
        ListNode *p1, *p2, *p3;
        ListNode *h3, *t3;
        p1 = l1;
        p2 = l2;
        h3 = t3 = NULL;
        while (p1 != NULL && p2 != NULL) {
            p3 = new ListNode(p1->val + p2->val);
            if (t3 == NULL) {
                h3 = t3 = p3;
            } else {
                t3->next = p3;
                t3 = p3;
            }
            p1 = p1->next;
            p2 = p2->next;
        }
        while (p1 != NULL) {
            t3->next = new ListNode(p1->val);
            t3 = t3->next;
            p1 = p1->next;
        }
        while (p2 != NULL) {
            t3->next = new ListNode(p2->val);
            t3 = t3->next;
            p2 = p2->next;
        }
        
        p3 = h3;
        while (p3->next != NULL) {
            p3->next->val += p3->val / R;
            p3->val %= R;
            p3 = p3->next;
        }
        while (p3->next == NULL && p3->val >= R) {
            p3->next = new ListNode(p3->val / R);
            p3->val %= R;
            p3 = p3->next;
        }
        
        return h3;
    }
};
