// Range modification, point query
#include <algorithm>
#include <vector>
using std::max;
using std::min;
using std::vector;

class BIT {
public:
    BIT(int _n = 0): n(_n), c(_n + 1, 0) {}
    
    void add(int idx, int val) {
        if (idx < 1 || idx > n) {
            return;
        }
        while (idx > 0) {
            c[idx] += val;
            idx -= lowbit(idx);
        }
    }
    
    void add(int idx1, int idx2, int val) {
        if (idx1 > idx2) {
            return;
        }
        add(idx1 - 1, -val);
        add(idx2, val);
    }
    
    int get(int idx) {
        if (idx < 1 || idx > n) {
            return 0;
        }
        int res = 0;
        while (idx <= n) {
            res += c[idx];
            idx += lowbit(idx);
        }
        return res;
    }
private:
    vector<int> c;
    int n;
    
    int lowbit(int x) {
        return x & -x;
    }
};

class Solution {
public:
    vector<int> getModifiedArray(int length, vector<vector<int>>& updates) {
        BIT bit(length);
        int i, j, val;
        for (auto &v: updates) {
            i = v[0];
            j = v[1];
            val = v[2];
            bit.add(i + 1, j + 1, val);
        }
        
        vector<int> res;
        for (i = 0; i < length; ++i) {
            res.push_back(bit.get(i + 1));
        }
        
        return res;
    }
};
