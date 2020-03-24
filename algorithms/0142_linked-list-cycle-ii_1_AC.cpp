/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <unordered_set>
using std::unordered_set;

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        unordered_set<ListNode *> us;
        ListNode *p = head;
        while (p != NULL) {
            if (us.find(p) == us.end()) {
                us.insert(p);
                p = p->next;
            } else {
                break;
            }
        }
        us.clear();
        return p;
    }
};
