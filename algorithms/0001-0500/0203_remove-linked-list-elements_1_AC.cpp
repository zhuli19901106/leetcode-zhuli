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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *p1;
        while (head != NULL && head->val == val) {
            p1 = head;
            head = head->next;
            delete p1;
        }
        if (head == NULL) {
            return head;
        }
        
        p1 = head;
        ListNode* p2;
        while (p1->next != NULL) {
            if (p1->next->val == val) {
                p2 = p1->next;
                p1->next = p2->next;
                delete p2;
            } else {
                p1 = p1->next;
            }
        }
        return head;
    }
};
