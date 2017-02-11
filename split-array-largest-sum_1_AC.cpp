// Seem like DP to me
#include <algorithm>
#include <climits>
#include <vector>
using std::max;
using std::min;
using std::vector;

class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        auto &a = nums;
        int n = a.size();
        m = min(m, n);
        vector<vector<int>> dp(m, vector<int>(n, INT_MAX));
        vector<int> s(n);
        
        int i;
        s[0] = a[0];
        for (i = 1; i < n; ++i) {
            s[i] = s[i - 1] + a[i];
        }
        dp[0] = s;

        int j, k;
        for (i = 1; i < m; ++i) {
            for (j = i; j < n; ++j) {
                for (k = i; k <= j; ++k) {
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][k - 1], s[j] - s[k - 1]));
                }
            }
        }
        
        int res = dp[m - 1][n - 1];
        dp.clear();
        s.clear();
        
        return res;
    }
};
