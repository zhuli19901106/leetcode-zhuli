#include <algorithm>
#include <vector>
using std::max;
using std::min;
using std::vector;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        auto &a = prices;
        int n = prices.size();
        if (n < 2) {
            return 0;
        }
        vector<int> v1(n, 0), v2(n, 0);
        int i;
        int min_val, max_val;
        int res;
        
        min_val = a[0];
        res = 0;
        for (i = 0; i <= n - 1; ++i) {
            res = max(res, a[i] - min_val);
            v1[i] = res;
            min_val = min(min_val, a[i]);
        }
        
        max_val = a[n - 1];
        res = 0;
        for (i = n - 1; i >= 0; --i) {
            res = max(res, max_val - a[i]);
            v2[i] = res;
            max_val = max(max_val, a[i]);
        }
        
        res = 0;
        for (i = 0; i <= n - 1; ++i) {
            res = max(res, v1[i] + v2[i]);
        }
        v1.clear();
        v2.clear();
        
        return res;
    }
};
