// Such consecutive counting problems can be handled in a similar way.
#include <algorithm>
#include <climits>
#include <unordered_map>
#include <vector>
using std::max;
using std::min;
using std::sort;
using std::unordered_map;
using std::vector;

class BIT {
public:
    BIT(int _n): n(_n), c(n + 1, 0) {}
    
    void add(int i, int val) {
        if (i < 1 || i > n) {
            return;
        }
        while (i <= n) {
            c[i] += val;
            i += lowbit(i);
        }
    }
    
    int sum(int i) {
        i = max(i, 0);
        i = min(i, n);
        int res = 0;
        while (i > 0) {
            res += c[i];
            i -= lowbit(i);
        }
        return res;
    }
    
    int sum(int i1, int i2) {
        if (i1 > i2) {
            return 0;
        }
        return sum(i2) - sum(i1);
    }
    
    ~BIT() {
        c.clear();
        n = 0;
    }
private:
    int n;
    vector<int> c;
    
    int lowbit(int x) {
        return x & -x;
    }
};

class Solution {
public:
    int reversePairs(vector<int>& nums) {
        vector<int64_t> v;
        unordered_map<int64_t, int> um;
        
        int n = nums.size();
        int i;
        for (i = 0; i < n; ++i) {
            um[nums[i]] = 0;
            um[nums[i] - 1LL] = 0;
            um[2LL * nums[i]] = 0;
        }
        um[INT_MIN] = 0;
        um[INT_MAX] = 0;
        
        for (auto it = um.begin(); it != um.end(); ++it) {
            v.push_back(it->first);
        }
        sort(v.begin(), v.end());
        
        n = v.size();
        for (i = 0; i < n; ++i) {
            um[v[i]] = i + 1;
        }
        
        BIT bit(n);
        int res = 0; 
        
        n = nums.size();
        for (i = n - 1; i >= 0; --i) {
            res += bit.sum(um[nums[i] - 1]);
            bit.add(um[2LL * nums[i]], 1);
        }
        um.clear();
        v.clear();
        
        return res;
    }
};
