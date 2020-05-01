// Linear DP
#include <algorithm>
#include <vector>
using std::min;
using std::vector;

class Solution {
public:
    int trap(vector<int>& height) {
        auto &a = height;
        int n = a.size();
        if (n < 3) {
            return 0;
        }
        
        vector<int> ll(n);
        vector<int> rr(n);
        int max_i;
        int max_val;
        int i;
        
        ll[0] = 0;
        max_i = 0;
        max_val = a[0];
        
        for (i = 1; i <= n - 1; ++i) {
            if (a[i] >= max_val) {
                max_i = i;
                max_val = a[i];
                ll[i] = i;
            } else {
                ll[i] = max_i;
            }
        }
        
        rr[n - 1] = n - 1;
        max_i = n - 1;
        max_val = a[n - 1];
        for (i = n - 2; i >= 0; --i) {
            if (a[i] >= max_val) {
                max_i = i;
                max_val = a[i];
                rr[i] = i;
            } else {
                rr[i] = max_i;
            }
        }
        
        int res = 0;
        for (i = 0; i < n; ++i) {
            res += min(a[ll[i]], a[rr[i]]) - a[i];
        }
        ll.clear();
        rr.clear();
        
        return res;
    }
};
