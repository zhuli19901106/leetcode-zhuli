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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if (head == NULL) {
            return head;
        }
        int cnt = 0;
        ListNode *h1, *t1, *h2, *t2, *h3, *t3;
        ListNode *p1, *p2;
        
        h1 = t1 = NULL;
        h2 = t2 = NULL;
        h3 = t3 = NULL;
        p1 = head;
        while (p1 != NULL) {
            ++cnt;
            p2 = p1;
            p1 = p1->next;
            p2->next = NULL;
            if (cnt < m) {
                insertTail(h1, t1, p2);
            } else if (cnt <= n) {
                insertHead(h2, t2, p2);
            } else {
                insertTail(h3, t3, p2);
            }
        }
        if (h1 != NULL) {
            t1->next = h2;
            t1 = t2;
        } else {
            h1 = h2;
            t1 = t2;
        }
        if (h3 != NULL) {
            t1->next = h3;
            t1 = t3;
        }
        return h1;
    }
private:
    void insertHead(ListNode *&head, ListNode *&tail, ListNode *node) {
        if (node == NULL) {
            return;
        }
        if (head == NULL) {
            head = tail = node;
            tail->next = NULL;
        } else {
            node->next = head;
            head = node;
        }
    }
    
    void insertTail(ListNode *&head, ListNode *&tail, ListNode *node) {
        if (node == NULL) {
            return;
        }
        if (tail == NULL) {
            head = tail = node;
        } else {
            tail->next = node;
            tail = node;
        }
        tail->next = NULL;
    }
};
