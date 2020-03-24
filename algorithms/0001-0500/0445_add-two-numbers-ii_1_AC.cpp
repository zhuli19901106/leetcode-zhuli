#include <algorithm>
#include <vector>
using std::max;
using std::vector;

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if (l1 == NULL) {
            return l2;
        }
        if (l2 == NULL) {
            return l1;
        }
        
        const int R = 10;
        
        int n1 = listLength(l1);
        int n2 = listLength(l2);
        vector<int> v;
        
        v.resize(max(n1, n2) + 1, 0);
        
        addList(l1, n1, v);
        addList(l2, n2, v);
        
        int i;
        int n3 = v.size();
        for (i = 1; i < n3; ++i) {
            v[i] += v[i- 1] / R;
            v[i - 1] %= R;
        }
        while (v.size() > 1 && v.back() == 0) {
            v.pop_back();
        }
        
        ListNode *l3, *t3;
        n3 = v.size();
        l3 = t3 = new ListNode(v[n3 - 1]);
        for (i = n3 - 2; i >= 0; --i) {
            t3->next = new ListNode(v[i]);
            t3 = t3->next;
        }
        return l3;
    }
private:
    int listLength(ListNode *head) {
        int n = 0;
        ListNode *ptr = head;
        while (ptr != NULL) {
            ptr = ptr->next;
            ++n;
        }
        return n;
    }
    
    void addList(ListNode *head, int len, vector<int> &v) {
        int i;
        ListNode *ptr = head;
        for (i = 0; i < len; ++i) {
            v[len - 1 - i] += ptr->val;
            ptr = ptr->next;
        }
    }
};
