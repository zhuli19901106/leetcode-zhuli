// Easy problem but hard to write perfect code.
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
    ListNode* swapPairs(ListNode* head) {
        if (head == NULL || head->next == NULL) {
            return head;
        }
        
        ListNode* new_head = NULL;
        ListNode* new_tail = NULL;
        
        new_head = head->next;
        new_tail = head;
        head = head->next->next;
        new_head->next = new_tail;
        new_tail->next = NULL;
        
        ListNode* p1;
        ListNode* p2;
        while (head != NULL && head->next != NULL) {
            p1 = head;
            p2 = head->next;
            head = head->next->next;
            new_tail->next = p2;
            p2->next = p1;
            new_tail = p1;
            new_tail->next = NULL;
        }
        if (head != NULL) {
            new_tail->next = head;
            new_tail = head;
            new_tail->next = NULL;
        }
        return new_head;
    }
};
