// O(n) space, straightforward solution.
/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
#include <unordered_map>
#include <vector>
using std::unordered_map;
using std::vector;

class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        if (head == NULL) {
            return NULL;
        }
        unordered_map<RandomListNode *, int> um;
        vector<RandomListNode *> v;
        int n = 0;
        RandomListNode *p1;
        
        p1 = head;
        while (p1 != NULL) {
            v.push_back(new RandomListNode(p1->label));
            if (v.size() > 1) {
                v[n - 1]->next = v[n];
            }
            um[p1] = n++;
            p1 = p1->next;
        }
        p1 = head;
        while (p1 != NULL) {
            if (p1->random != NULL) {
                v[um[p1]]->random = v[um[p1->random]];
            }
            p1 = p1->next;
        }
        RandomListNode *new_head = v[0];
        um.clear();
        v.clear();
        
        return new_head;
    }
};
