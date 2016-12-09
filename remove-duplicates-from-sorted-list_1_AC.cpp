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
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == NULL) {
            return head;
        }
        ListNode* ptr = head;
        ListNode* tmp;
        while (ptr->next != NULL) {
            if (ptr->val == ptr->next->val) {
                tmp = ptr->next;
                ptr->next = tmp->next;
                delete tmp;
            } else {
                ptr = ptr->next;
            }
        }
        return head;
    }
};
