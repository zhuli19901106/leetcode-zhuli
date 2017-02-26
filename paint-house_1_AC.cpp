// Traditional DP
#include <algorithm>
#include <climits>
#include <vector>
using std::min;
using std::vector;

class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        static const int NUM_COLOR = 3;
        
        auto &c = costs;
        int n = c.size();
        if (n == 0) {
            return 0;
        }
        
        vector<vector<int>> dp(n, vector<int>(NUM_COLOR, 0));
        int i;
        for (i = 0; i < NUM_COLOR; ++i) {
            dp[0][i] = c[0][i];
        }
        
        int j, k;
        for (i = 1; i < n; ++i) {
            for (j = 0; j < NUM_COLOR; ++j) {
                dp[i][j] = INT_MAX;
                for (k = 0; k < NUM_COLOR; ++k) {
                    if (j == k) {
                        continue;
                    }
                    dp[i][j] = min(dp[i][j], dp[i - 1][k]);
                }
                dp[i][j] += c[i][j];
            }
        }
        
        int res = INT_MAX;
        for (i = 0; i < NUM_COLOR; ++i) {
            res = min(res, dp[n - 1][i]);
        }
        dp.clear();
        
        return res;
    }
};
