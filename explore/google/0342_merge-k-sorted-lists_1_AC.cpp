// Use the heap
// 1AC, very smooth
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <queue>
using std::priority_queue;

typedef struct ListNodeComp {
    bool operator () (const ListNode *n1, const ListNode *n2) const {
        return n1->val > n2->val;
    }
} ListNodeComp;

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode *, vector<ListNode *>, ListNodeComp> pq;
        int n = lists.size();
        int i;
        for (i = 0; i < n; ++i) {
            if (lists[i] == NULL) {
                continue;
            }
            pq.push(lists[i]);
        }
        
        ListNode *head, *tail;
        ListNode *ptr;
        
        head = tail = NULL;
        while (!pq.empty()) {
            ptr = pq.top();
            pq.pop();
            if (ptr->next != NULL) {
                pq.push(ptr->next);
            }
            ptr->next = NULL;
            insertTail(head, tail, ptr);
        }
        
        return head;
    }
private:
    void insertTail(ListNode *&head, ListNode *&tail, ListNode *ptr) {
        if (ptr == NULL) {
            return;
        }
        if (tail == NULL) {
            head = ptr;
        } else {
            tail->next = ptr;
        }
        tail = ptr;
        tail->next = NULL;
    }
};
