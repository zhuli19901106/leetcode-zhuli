// DP with space optimized
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
        vector<vector<int>> dl(2, vector<int>(n, 0));
        // Global optimum
        vector<vector<int>> dg(2, vector<int>(n, 0));
        
        int diff;
        int min_val = a[0];
        for (i = 1; i < n; ++i) {
            diff = max(0, a[i] - min_val);
            dl[0][i] = diff;
            dg[0][i] = max(dg[0][i - 1], dl[0][i]);
            min_val = min(min_val, a[i]);
        }
        
        int f, nf;
        int j, ki;
        
        f = 1;
        nf = !f;
        for (ki = 1; ki < k; ++ki) {
            fill(dl[f].begin(), dl[f].end(), 0);
            fill(dg[f].begin(), dg[f].end(), 0);
            for (i = ki + 1; i < n; ++i) {
                diff = max(0, a[i] - a[ki]);
                dg[f][i] = dl[f][i] = dg[nf][ki] + diff;
                for (j = ki + 1; j < i; ++j) {
                    diff = max(0, a[i] - a[j]);
                    dl[f][i] = max(dl[f][i], dg[nf][j] + diff);
                }
                dg[f][i] = max(dg[f][i - 1], dl[f][i]);
            }
            f = !f;
            nf = !f;
        }
        int res = dg[nf][n - 1];
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