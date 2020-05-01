/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <algorithm>
using std::swap;

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *h1 = headA;
        ListNode *h2 = headB;
        int n1 = listLength(h1);
        int n2 = listLength(h2);
        
        if (n1 == 0 || n2 == 0) {
            return NULL;
        }
        if (n1 > n2) {
            swap(h1, h2);
            swap(n1, n2);
        }
        
        int i;
        for (i = n1; i < n2; ++i) {
            h2 = h2->next;
        }
        while (h1 != h2) {
            h1 = h1->next;
            h2 = h2->next;
        }
        return h1;
    }
private:
    int listLength(ListNode *h) {
        if (h == NULL) {
            return 0;
        }
        int cnt = 0;
        while (h != NULL) {
            h = h->next;
            ++cnt;
        }
        return cnt;
    }
};