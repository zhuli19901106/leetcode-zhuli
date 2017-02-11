#include <algorithm>
#include <unordered_set>
#include <vector>
using std::max;
using std::min;
using std::unordered_set;
using std::vector;

class Solution {
public:
    int maximumGap(vector<int>& nums) {
        auto &a = nums;
        int n = a.size();
        if (n == 0) {
            return 0;
        }
        
        unordered_set<int> us;
        int max_val = a[0];
        int min_val = a[0];
        int i;
        for (i = 0; i < n; ++i) {
            max_val = max(max_val, a[i]);
            min_val = min(min_val, a[i]);
            us.insert(a[i]);
        }
        
        int m = us.size();
        us.clear();
        if (m == 1) {
            return 0;
        }
        
        // m buckets
        int d = (max_val - min_val + m - 2) / (m - 1);
        vector<int> v1(m), v2(m);
        vector<bool> vb(m, false);
        
        int j;
        for (i = 0; i < n; ++i) {
            j = (a[i] - min_val) / d;
            if (vb[j]) {
                v1[j] = min(v1[j], a[i]);
                v2[j] = max(v2[j], a[i]);
            } else {
                vb[j] = true;
                v1[j] = v2[j] = a[i];
            }
        }
        
        int res = 0;
        i = 0;
        while (true) {
            while (i < m && !vb[i]) {
                ++i;
            }
            j = i + 1;
            while (j < m && !vb[j]) {
                ++j;
            }
            if (i < m && j < m) {
                res = max(res, v1[j] - v2[i]);
                i = j;
            } else {
                break;
            }
        }
        vb.clear();
        v1.clear();
        v2.clear();
        
        return res;
    }
};
