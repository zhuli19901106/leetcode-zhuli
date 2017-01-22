// It's good practice to encapsulate some list operations.
// Otherwise the code is gonna get ugly and twisting.
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
            return NULL;
        }
        ListNode *p1, *p2;
        ListNode *h, *t;
        
        p1 = head;
        h = t = NULL;
        while (p1 != NULL) {
            p2 = p1->next;
            if (p2 == NULL || p1->val != p2->val) {
                insertTail(h, t, p1);
                p1 = p2;
                continue;
            }
            while (p1->next != NULL && p1->val == (p2 = p1->next)->val) {
                p1->next = p2->next;
                delete p2;
            }
            p2 = p1->next;
            delete p1;
            p1 = p2;
        }
        return h;
    }
private:
    void insertTail(ListNode *&head, ListNode *&tail, ListNode *ptr) {
        if (tail == NULL) {
            head = tail = ptr;
        } else {
            tail->next = ptr;
            tail = ptr;
        }
        tail->next = NULL;
    }
};
