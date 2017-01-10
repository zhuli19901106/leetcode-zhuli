// 59 ms
// O(n ^ 3) DP solution, I got stuck for about two hours.
// But still haven't grabbed the idea of a better solution.
#include <algorithm>
#include <climits>
#include <vector>
using std::max;
using std::min;
using std::vector;

class Solution {
public:
    int getMoneyAmount(int n) {
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, INT_MAX));
        int i, j, k;
        
        for (i = 1; i <= n; ++i) {
            dp[i][i] = 0;
        }
        for (i = 1; i < n; ++i) {
            for (j = 1; j + i <= n; ++j) {
                dp[j][j + i] = j + dp[j + 1][j + i];
                for (k = j + 1; k < j + i; ++k) {
                    dp[j][j + i] = min(dp[j][j + i], k + max(dp[j][k - 1], dp[k + 1][j + i]));
                }
                dp[j][j + i] = min(dp[j][j + i], j + i + dp[j][j + i - 1]);
            }
        }
        int ret = dp[1][n];
        dp.clear();
        return ret;
    }
};
