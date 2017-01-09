// Multi-dimensional knapsack problem
#include <algorithm>
using std::max;

class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        int cnt = strs.size();
        vector<vector<int>> c(2, vector<int>(cnt, 0));
        int i;
        int j;
        int ls;
        for (i = 0; i < cnt; ++i) {
            ls = strs[i].size();
            for (j = 0; j < ls; ++j) {
                ++c[strs[i][j] - '0'][i];
            }
        }
        
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, -1));
        dp[0][0] = 0;
        int k;
        for (k = 0; k < cnt; ++k) {
            for (i = m; i >= c[0][k];  --i) {
                for (j = n; j >= c[1][k]; --j) {
                    if (dp[i - c[0][k]][j - c[1][k]] == -1) {
                        continue;
                    }
                    dp[i][j] = max(dp[i][j], dp[i - c[0][k]][j - c[1][k]] + 1);
                }
            }
        }
        int res = 0;
        for (i = 0; i <= m; ++i) {
            for (j = 0; j <= n; ++j) {
                res = max(res, dp[i][j]);
            }
        }
        
        c.clear();
        dp.clear();
        return res;
    }
};
