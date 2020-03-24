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
    ListNode* partition(ListNode* head, int x) {
        ListNode *h1, *t1, *h2, *t2;
        
        h1 = t1 = NULL;
        h2 = t2 = NULL;
        ListNode *p;
        
        while (head != NULL) {
            p = head;
            head = head->next;
            p->next = NULL;
            if (p->val < x) {
                appendNode(p, h1, t1);
            } else {
                appendNode(p, h2, t2);
            }
        }
        if (h1 != NULL) {
            t1->next = h2;
            return h1;
        } else {
            return h2;
        }
    }
private:
    void appendNode(ListNode *node, ListNode *&head, ListNode *&tail) {
        if (head == NULL) {
            head = tail = node;
        } else {
            tail->next = node;
            tail = node;
        }
        tail->next = NULL;
    }
};
