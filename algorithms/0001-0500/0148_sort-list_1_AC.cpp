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
    ListNode* sortList(ListNode* head) {
        int n = 0;
        ListNode *p1;
        
        p1 = head;
        while (p1 != NULL) {
            p1 = p1->next;
            ++n;
        }
        if (n < 2) {
            return head;
        }
        
        int m;
        int i;
        ListNode *h1, *t1, *h2, *t2;
        ListNode *h3, *t3, *h4, *t4;
        ListNode *p;
        
        m = 1;
        while (m < n) {
            p = head;
            h4 = t4 = NULL;
            while (head != NULL) {
                h1 = t1 = NULL;
                for (i = 0; head != NULL && i < m; ++i) {
                    p = head;
                    head = head->next;
                    p->next = NULL;
                    insertTail(h1, t1, p);
                }
                h2 = t2 = NULL;
                for (i = 0; head != NULL && i < m; ++i) {
                    p = head;
                    head = head->next;
                    p->next = NULL;
                    insertTail(h2, t2, p);
                }
                h3 = t3 = NULL;
                mergeList(h3, t3, h1, t1, h2, t2);
                appendList(h4, t4, h3, t3);
            }
            head = h4;
            m <<= 1;
        }
        return head;
    }
private:
    void insertTail(ListNode *&head, ListNode *&tail, ListNode *ptr) {
        if (ptr == NULL) {
            return;
        }
        if (tail == NULL) {
            head = tail = ptr;
        } else {
            tail->next = ptr;
            tail = ptr;
        }
        tail->next = NULL;
    }
    
    void mergeList(ListNode *&head, ListNode *&tail, 
        ListNode *h1, ListNode *t1, ListNode *h2, ListNode *t2) {
        if (t1 == NULL) {
            head = h2;
            tail = t2;
            return;
        } else if (t2 == NULL) {
            head = h1;
            tail = t1;
            return;
        }
        ListNode *p;
        while (h1 != NULL && h2 != NULL) {
            if (h1->val < h2->val) {
                p = h1;
                h1 = h1->next;
                p->next = NULL;
            } else {
                p = h2;
                h2 = h2->next;
                p->next = NULL;
            }
            insertTail(head, tail, p);
        }
        if (h1 != NULL) {
            tail->next = h1;
            tail = t1;
        }
        if (h2 != NULL) {
            tail->next = h2;
            tail = t2;
        }
    }
    
    void appendList(ListNode *&head, ListNode *&tail, ListNode *h1, ListNode *t1) {
        if (tail == NULL) {
            head = h1;
            tail = t1;
        } else {
            tail->next = h1;
            tail = t1;
        }
    }
};
