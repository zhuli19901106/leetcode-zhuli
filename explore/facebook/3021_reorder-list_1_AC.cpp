// 1AC
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
    void reorderList(ListNode* head) {
        if (head == NULL || head->next == NULL) {
            return;
        }
        ListNode *p1, *p2;
        
        p1 = p2 = head;
        while (p2->next != NULL && p2->next->next != NULL) {
            p1 = p1->next;
            p2 = p2->next->next;
        }
        ListNode *h1 = head;
        ListNode *h2 = p1->next;
        p1->next = NULL;
        
        ListNode *h3, *t3;
        h2 = reverseList(h2);
        h3 = t3 = NULL;
        while (h1 != NULL && h2 != NULL) {
            p1 = h1;
            h1 = h1->next;
            insertTail(h3, t3, p1);
            
            p2 = h2;
            h2 = h2->next;
            insertTail(h3, t3, p2);
        }
        if (h1 != NULL) {
            t3->next = h1;
        }
        if (h2 != NULL) {
            t3->next = h2;
        }
        while (t3->next != NULL) {
            t3 = t3->next;
        }
    }
private:
    ListNode *reverseList(ListNode *head) {
        ListNode *h, *t;
        ListNode *p;
        
        h = t = NULL;
        while (head != NULL) {
            p = head;
            head = head->next;
            insertHead(h, t, p);
        }
        return h;
    }
    
    void insertHead(ListNode *&head, ListNode *&tail, ListNode *p) {
        if (p == NULL) {
            return;
        }
        if (tail == NULL) {
            head = tail = p;
            tail->next = NULL;
        } else {
            p->next = head;
            head = p;
        }
    }
    
    void insertTail(ListNode *&head, ListNode *&tail, ListNode *p) {
        if (p == NULL) {
            return;
        }
        if (tail == NULL) {
            head = tail = p;
        } else {
            tail->next = p;
            tail = p;
        }
        tail->next = NULL;
    }
};
