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
    vector<ListNode*> splitListToParts(ListNode* root, int k) {
        int n = 0;
        ListNode *p1;
        p1 = root;
        while (p1 != NULL) {
            p1 = p1->next;
            ++n;
        }
        
        int m = n / k;
        int k1 = n % k;
        int k2 = k - k1;
        vector<ListNode *> res;
        
        int i;
        for (i = 0; i < k1; ++i) {
            splitList(root, res, m + 1);
        }
        for (i = 0; i < k2; ++i) {
            splitList(root, res, m);
        }
        return res;
    }
private:
    void splitList(ListNode *&root, vector<ListNode *> &res, int n) {
        ListNode *h, *t;
        ListNode *p1;
        int i;
        
        p1 = root;
        h = t = NULL;
        for (i = 0; i < n && root != NULL; ++i) {
            root = root->next;
            p1->next = NULL;
            if (t == NULL) {
                h = p1;
            } else {
                t->next = p1;
            }
            t = p1;
            p1 = root;
        }
        res.push_back(h);
    }
};
