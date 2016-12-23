// Reservoir sampling
#include <cstdlib>
using std::rand;
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
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head) {
        this->head = head;
    }
    
    /** Returns a random node's value. */
    int getRandom() {
        if (head == NULL) {
            return 0;
        }
        
        int res = head->val;
        ListNode *cur = head->next;
        int count = 1;
        while (cur != NULL) {
            ++count;
            if (rand() % count == 0) {
                res = cur->val;
            }
            cur = cur->next;
        }
        return res;
    }
private:
    ListNode *head;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */
