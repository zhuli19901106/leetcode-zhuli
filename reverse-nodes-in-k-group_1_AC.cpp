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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (head == NULL || head->next == NULL || k < 2) {
            return head;
        }
        
        ListNode *h1, *t1;
        ListNode *h2, *t2;
        int cnt = 0;
        
        h1 = t1 = NULL;
        while (head != NULL) {
            cnt = getList(head, h2, t2, k);
            if (cnt >= k) {
                reverseList(h2, t2);
            }
            if (t1 == NULL) {
                h1 = h2;
            } else {
                t1->next = h2;
            }
            t1 = t2;
        }
        head = h1;
        return head;
    }
private:
    int getList(ListNode *&head, ListNode *&h, ListNode *&t, int k) {
        h = t = NULL;
        if (head == NULL) {
            return 0;
        }
        
        int cnt = 0;
        ListNode *p = head;
        while (cnt < k && p != NULL) {
            head = head->next;
            if (t == NULL) {
                h = t = p;
            } else {
                t->next = p;
                t = p;
            }
            t->next = NULL;
            ++cnt;
            p = head;
        }
        return cnt;
    }
    
    void reverseList(ListNode *&head, ListNode *&tail) {
        if (head == NULL) {
            return;
        }
        ListNode *h, *t;
        ListNode *p;
        
        h = t = NULL;
        p = head;
        while (p != NULL) {
            head = head->next;
            if (h == NULL) {
                h = t = p;
                t->next = NULL;
            } else {
                p->next = h;
                h = p;
            }
            p = head;
        }
        head = h;
        tail = t;
    }
};
