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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (l1 == NULL) {
            return l2;
        }
        if (l2 == NULL) {
            return l1;
        }
        if (l1->val > l2->val) {
            return mergeTwoLists(l2, l1);
        }
        
        ListNode *l3 = l1;
        ListNode *t3 = l3;
        l1 = l1->next;
        t3->next = NULL;
        
        while (l1 != NULL && l2 != NULL) {
            if (l1->val < l2->val) {
                t3->next = l1;
                l1 = l1->next;
            } else {
                t3->next = l2;
                l2 = l2->next;
            }
            t3 = t3->next;
            t3->next = NULL;
        }
        if (l1 != NULL) {
            t3->next = l1;
            l1 = NULL;
        }
        if (l2 != NULL) {
            t3->next = l2;
            l2 = NULL;
        }
        return l3;
    }
};
