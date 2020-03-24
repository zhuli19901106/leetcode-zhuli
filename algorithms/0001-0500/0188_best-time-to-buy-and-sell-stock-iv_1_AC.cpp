// DP without space optimization
// Make sure you understand the relationship between global and local.
#include <algorithm>
#include <vector>
using std::max;
using std::min;
using std::vector;

class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        if (k == 0) {
            return 0;
        }
        auto &a = prices;
        int n = a.size();
        int cnt = 0;
        int i;
        for (i = 0; i + 1 < n; ++i) {
            if (a[i] < a[i + 1]) {
                ++cnt;
            }
        }
        if (cnt <= k) {
            // Greed is good
            return maxProfitAny(a);
        }
        
        // Local optimum
        vector<vector<int>> dl(k, vector<int>(n, 0));
        // Global optimum
        vector<vector<int>> dg(k, vector<int>(n, 0));
        
        int diff;
        int min_val = a[0];
        for (i = 1; i < n; ++i) {
            diff = max(0, a[i] - min_val);
            dl[0][i] = diff;
            dg[0][i] = max(dg[0][i - 1], dl[0][i]);
            min_val = min(min_val, a[i]);
        }
        
        int j, ki;
        for (ki = 1; ki < k; ++ki) {
            for (i = ki + 1; i < n; ++i) {
                diff = max(0, a[i] - a[ki]);
                dg[ki][i] = dl[ki][i] = dg[ki - 1][ki] + diff;
                for (j = ki + 1; j < i; ++j) {
                    diff = max(0, a[i] - a[j]);
                    dl[ki][i] = max(dl[ki][i], dg[ki - 1][j] + diff);
                }
                dg[ki][i] = max(dg[ki][i - 1], dl[ki][i]);
            }
        }
        int res = dg[k - 1][n - 1];
        dg.clear();
        dl.clear();
        
        return res;
    }
private:
    int maxProfitAny(vector<int>& prices) {
        auto &a = prices;
        int n = a.size();
        int res = 0;
        int i;
        for (i = 0; i + 1 < n; ++i) {
            if (a[i] < a[i + 1]) {
                res += a[i + 1] - a[i];
            }
        }
        
        return res;
    }
};