/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        if (head == NULL) {
            return NULL;
        }
        if (head->next == NULL) {
            return new TreeNode(head->val);
        }
        TreeNode *root;
        if (head->next->next == NULL) {
            root = new TreeNode(head->val);
            root->right = new TreeNode(head->next->val);
            return root;
        }
        
        ListNode *p1, *p2;
        p1 = head;
        p2 = head->next;
        while (p2->next != NULL && p2->next->next != NULL) {
            p1 = p1->next;
            p2 = p2->next->next;
        }
        p2 = p1->next;
        p1->next = NULL;
        
        root = new TreeNode(p2->val);
        root->left = sortedListToBST(head);
        root->right = sortedListToBST(p2->next);
        p1->next = p2;
        return root;
    }
};
