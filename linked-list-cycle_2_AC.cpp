// Hash and check.
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
    bool hasCycle(ListNode *head) {
        unordered_set<ListNode *> us;
        
        while (head != NULL) {
            if (us.find(head) == us.end()) {
                us.insert(head);
            } else {
                break;
            }
            head = head->next;
        }
        us.clear();
        return head != NULL;
    }
};
