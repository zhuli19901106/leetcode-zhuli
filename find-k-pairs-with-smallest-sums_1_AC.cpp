#include <queue>
using std::priority_queue;

typedef struct Pair {
    vector<int> *a1, *a2;
    int i1, i2;
    
    bool operator < (const Pair &p) const {
        return (*a1)[i1] + (*a2)[i2] < (*p.a1)[p.i1] + (*p.a2)[p.i2];
    }
    
    bool operator > (const Pair &p) const {
        return (*a1)[i1] + (*a2)[i2] > (*p.a1)[p.i1] + (*p.a2)[p.i2];
    }
    
    bool operator == (const Pair &p) const {
        return (*a1)[i1] + (*a2)[i2] == (*p.a1)[p.i1] + (*p.a2)[p.i2];
    }
} Pair;

class Solution {
public:
    vector<pair<int, int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<pair<int, int>> res;
        vector<int> &a1 = nums1;
        vector<int> &a2 = nums2;
        int n1 = a1.size();
        int n2 = a2.size();
        if (n1 == 0 || n2 == 0) {
            return res;
        }
        
        priority_queue<Pair, vector<Pair>, greater<Pair>> pq;
        int i;
        Pair p;
        
        p.a1 = &a1;
        p.a2 = &a2;
        for (i = 0; i < n1; ++i) {
            p.i1 = i;
            p.i2 = 0;
            pq.push(p);
        }
        for (i = 0; i < k && !pq.empty(); ++i) {
            p = pq.top();
            pq.pop();
            res.push_back(make_pair((*p.a1)[p.i1], (*p.a2)[p.i2]));
            ++p.i2;
            if (p.i2 < (*p.a2).size()) {
                pq.push(p);
            }
        }
        while (!pq.empty()) {
            pq.pop();
        }
        return res;
    }
};
