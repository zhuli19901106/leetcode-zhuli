// Seem like DP to me
// Space optimized to O(n)
#include <algorithm>
#include <climits>
#include <vector>
using std::fill;
using std::max;
using std::min;
using std::vector;

class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        auto &a = nums;
        int n = a.size();
        m = min(m, n);
        vector<vector<int>> dp(2, vector<int>(n));
        vector<int> s(n);
        
        int i;
        s[0] = a[0];
        for (i = 1; i < n; ++i) {
            s[i] = s[i - 1] + a[i];
        }
        dp[0] = s;
        
        int f, nf;
        int j, k;
        
        f = 1;
        nf = !f;
        for (i = 1; i < m; ++i) {
            fill(dp[f].begin(), dp[f].end(), INT_MAX);
            for (j = i; j < n; ++j) {
                for (k = i; k <= j; ++k) {
                    dp[f][j] = min(dp[f][j], max(dp[nf][k - 1], s[j] - s[k - 1]));
                }
            }
            f = !f;
            nf = !f;
        }
        
        int res = dp[nf][n - 1];
        dp.clear();
        s.clear();
        
        return res;
    }
};
