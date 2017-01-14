#include <algorithm>
#include <climits>
using std::min;

class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> vp;
        vector<int> vi(3, 0);
        vector<int> res;
        
        vp.push_back(2);
        vp.push_back(3);
        vp.push_back(5);
        
        res.push_back(1);
        int i, j;
        int new_val;
        int vp_len = vp.size();
        for (i = 1; i < n; ++i) {
            new_val = INT_MAX;
            for (j = 0; j < vp_len; ++j) {
                new_val = min(new_val, vp[j] * res[vi[j]]);
            }
            res.push_back(new_val);
            for (j = 0; j < vp_len; ++j) {
                if (new_val == vp[j] * res[vi[j]]) {
                    ++vi[j];
                }
            }
        }
        return res[n - 1];
    }
};
