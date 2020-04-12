// Careful with the pointer.
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int cnt = n + 1;
        ListNode* p1 = head;
        while (p1 != NULL && cnt > 0) {
            p1 = p1->next;
            --cnt;
        }
        ListNode *tmp; 
        if (cnt > 0) {
            tmp = head;
            head = head->next;
            delete tmp;
            return head;
        }
        ListNode *p2 = head;
        while (p1 != NULL) {
            p1 = p1->next;
            p2 = p2->next;
        }
        tmp = p2->next;
        p2->next = tmp->next;
        delete tmp;
        return head;
    }
};
