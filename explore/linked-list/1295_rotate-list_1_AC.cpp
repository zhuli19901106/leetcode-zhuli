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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == NULL || head->next == NULL) {
            return head;
        }
        int n = 0;
        ListNode *p1 = head;
        while (p1 != NULL) {
            p1 = p1->next;
            ++n;
        }
        if (k % n == 0) {
            return head;
        }
        k %= n;
        
        ListNode *h, *t;
        int i;
        
        p1 = head;
        for (i = 1; i < n - k; ++i) {
            p1 = p1->next;
        }
        h = p1->next;
        p1->next = NULL;
        
        t = h;
        while (t->next != NULL) {
            t = t->next;
        }
        t->next = head;
        
        return h;
    }
};
