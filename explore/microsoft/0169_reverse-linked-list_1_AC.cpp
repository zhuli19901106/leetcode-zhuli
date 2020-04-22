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
    ListNode* reverseList(ListNode* head) {
        if (head == NULL) {
            return head;
        }
        ListNode *new_head;
        
        new_head = head;
        head = head->next;
        new_head->next = NULL;
        ListNode *ptr;
        while (head != NULL) {
            ptr = head;
            head = head->next;
            ptr->next = new_head;
            new_head = ptr;
        }
        return new_head;
    }
};
