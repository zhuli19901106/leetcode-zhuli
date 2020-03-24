// O(n * log^2 (n)) solution using binary indexed tree and binary search.
// It took me more than an hour to think it through.
// Algorithmic problems like this are both challenging and frustrating.
// I think this one is "hard", not "medium".
#include <algorithm>
#include <utility>
using std::make_pair;
using std::max;
using std::min;
using std::sort;

typedef pair<int, int> PII;

class BIT {
public:
    // Binary indexed tree, indexing from 1
    BIT(int n) {
        this->n = n;
        v.resize(n + 1, 0);
    }
    
    // Add val to v[idx];
    void update(int idx, int val) {
        if (idx < 1 || idx > n) {
            return;
        }
        int i = idx;
        while (i <= n) {
            v[i] += val;
            i += lowbit(i);
        }
    }
    
    // Sum from v[1] to v[idx]
    int sum(int idx) {
        idx = max(idx, 0);
        idx = min(idx, n);
        int i = idx;
        int res = 0;
        while (i > 0) {
            res += v[i];
            i -= lowbit(i);
        }
        return res;
    }
    
    int get(int idx) {
        if (idx < 1 || idx > n) {
            return 0;
        }
        return sum(idx) - sum(idx - 1);
    }
    
    // Find the index of the first element greater than val
    int upperBound(int val) {
        if (sum(1) > val) {
            return 1;
        }
        if (sum(n) <= val) {
            return n + 1;
        }
        int ll = 1;
        int rr = n;
        int mm;
        while (rr - ll > 1) {
            mm = ll + (rr - ll >> 1);
            if (sum(mm) <= val) {
                ll = mm;
            } else {
                rr = mm;
            }
        }
        return rr;
    }
    
    int size() {
        return n;
    }
    
    ~BIT() {
        v.clear();
    }
private:
    int n;
    vector<int> v;
    
    int lowbit(int x) {
        return x & -x;
    }
};

bool comparator(const PII &p1, const PII &p2)
{
    if (p1.first != p2.first) {
        return p1.first < p2.first;
    }
    if (p1.second != p2.second) {
        return p1.second > p2.second;
    }
    return true;
}

class Solution {
public:
    vector<PII> reconstructQueue(vector<PII>& people) {
        int n = people.size();
        sort(people.begin(), people.end(), comparator);
        
        vector<PII> res(n, make_pair(-1, -1));
        BIT bit(n);
        int i;
        for (i = 1; i <= n; ++i) {
            bit.update(i, 1);
        }
        int j;
        for (i = 0; i < n; ++i) {
            j = bit.upperBound(people[i].second);
            bit.update(j, -1);
            res[j - 1] = people[i];
        }
        return res;
    }
};
