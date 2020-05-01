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
    ListNode* oddEvenList(ListNode* head) {
        ListNode *h[2], *t[2];
        ListNode *p = head;
        int f = 0;
        
        h[0] = t[0] = NULL;
        h[1] = t[1] = NULL;
        while (p != NULL) {
            if (h[f] == NULL) {
                h[f] = p;
            } else {
                t[f]->next = p;
            }
            t[f] = p;
            p = p->next;
            t[f]->next = NULL;
            f = !f;
        }
        if (t[0] != NULL) {
            t[0]->next = h[1];
        }
        return h[0];
    }
};
