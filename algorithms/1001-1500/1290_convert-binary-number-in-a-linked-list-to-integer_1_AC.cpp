// easy
// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
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
    int getDecimalValue(ListNode* head) {
        int res = 0;
        ListNode *ptr = head;
        while (ptr != nullptr) {
            res = (res << 1) + ptr->val;
            ptr = ptr->next;
        }
        return res;
    }
};
