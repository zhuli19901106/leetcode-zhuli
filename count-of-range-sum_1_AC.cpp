// Think about the clever use of "1" and "-1".
#include <algorithm>
#include <cstdint>
#include <map>
#include <vector>
using std::max;
using std::min;
using std::map;
using std::vector;

class BIT {
public:
    BIT(int _n = 0): n(_n) {
        c.resize(n + 1, 0);
    }
    
    void add(int idx, int64_t val) {
        if (idx < 1 || idx > n) {
            return;
        }
        while (idx <= n) {
            c[idx] += val;
            idx += lowbit(idx);
        }
    }
    
    int64_t sum(int idx) {
        idx = max(idx, 0);
        idx = min(idx, n);
        int64_t res = 0;
        while (idx >= 1) {
            res += c[idx];
            idx -= lowbit(idx);
        }
        return res;
    }
private:
    vector<int64_t> c;
    int n;
    
    int lowbit(int x) {
        return x & -x;
    }
};

class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        auto &a = nums;
        int n = a.size();
        int i;
        int64_t s = 0;
        map<int64_t, int> mm;
        
        mm[lower] = 0;
        mm[upper + 1] = 0;
        for (i = 0; i < n; ++i) {
            s += a[i];
            mm[s] = 0;
            mm[s + lower] = 0;
            mm[s + upper + 1] = 0;
        }
        
        i = 0;
        for (auto it = mm.begin(); it != mm.end(); ++it) {
            it->second = ++i;
        }
        
        BIT bit(i);
        int64_t res = 0;
        
        s = 0;
        bit.add(mm[lower], 1);
        bit.add(mm[upper + 1], -1);
        for (i = 0; i < n; ++i) {
            s += a[i];
            res += bit.sum(mm[s]);
            bit.add(mm[s + lower], 1);
            bit.add(mm[s + upper + 1], -1);
        }
        mm.clear();
        
        return res;
    }
};
