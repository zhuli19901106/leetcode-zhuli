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
    bool isPalindrome(ListNode* head) {
        int n = listLength(head);
        if (n <= 1) {
            return true;
        }
        
        ListNode *h1 = head;
        ListNode *h2 = head;
        ListNode *t1;
        int i;
        for (i = 1; i < n / 2; ++i) {
            h2 = h2->next;
        }
        t1 = h2;
        h2 = t1->next;
        t1->next = NULL;
        h2 = reverseList(h2);
        
        ListNode *p1 = h1;
        ListNode *p2 = h2;
        for (i = 0; i < n / 2; ++i) {
            if (p1->val != p2->val) {
                break;
            }
            p1 = p1->next;
            p2 = p2->next;
        }
        h2 = reverseList(h2);
        t1->next = h2;
        return i == n / 2;
    }
private:
    int listLength(ListNode* head) {
        ListNode* ptr = head;
        int n = 0;
        while (ptr != NULL) {
            ptr = ptr->next;
            ++n;
        }
        return n;
    }
    
    ListNode* reverseList(ListNode* head) {
        if (head == NULL) {
            return head;
        }
        
        ListNode *h1 = head;
        ListNode *p1 = head->next;
        ListNode *p2;
        
        h1->next = NULL;
        while (p1 != NULL) {
            p2 = p1->next;
            p1->next = h1;
            h1 = p1;
            p1 = p2;
        }
        return h1;
    }
};
