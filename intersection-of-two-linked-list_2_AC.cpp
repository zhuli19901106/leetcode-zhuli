// O(1) space solution
// Cover every possible condition, otherwise there's gonna be bugs.
#include <unordered_set>
using std::unordered_set;
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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (headA == NULL || headB == NULL) {
            return NULL;
        }
        if (getTail(headA) != getTail(headB)) {
            return NULL;
        }
        
        int n1, n2, n3;
        n1 = listLength(headA) - 1;
        n2 = listLength(headB) - 1;
        headA = reverseList(headA);
        n3 = listLength(headB);
        headA = reverseList(headA);
        
        int n = (n1 + n3 - n2) / 2;
        int i;
        ListNode *ptr = headA;
        for (i = 0; i < n; ++i) {
            ptr = ptr->next;
        }
        return ptr;
    }
private:
    int listLength(ListNode *head) {
        ListNode *ptr = head;
        int n = 0;
        while (ptr != NULL) {
            ptr = ptr->next;
            ++n;
        }
        return n;
    }
    
    ListNode *reverseList(ListNode *head) {
        if (head == NULL) {
            return head;
        }
        ListNode *h = head;
        ListNode *p1 = head->next;
        ListNode *p2;
        
        h->next = NULL;
        while (p1 != NULL) {
            p2 = p1->next;
            p1->next = h;
            h = p1;
            p1 = p2;
        }
        return h;
    }
    
    ListNode *getTail(ListNode *head) {
        if (head == NULL) {
            return head;
        }
        ListNode *ptr = head;
        while (ptr->next != NULL) {
            ptr = ptr->next;
        }
        return ptr;
    }
};
