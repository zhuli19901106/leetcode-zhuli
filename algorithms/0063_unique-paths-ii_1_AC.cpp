// Leetcode has just added integer overflow detection, so watch out.
#include <cstdint>

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int n = obstacleGrid.size();
        int m = (n > 0 ? obstacleGrid[0].size() : 0);
        if (n == 0 || m == 0) {
            return 0;
        }
        
        vector<vector<int64_t>> dp(2, vector<int64_t>(m + 1));
        int i, j;
        int f, nf;
        
        dp[0][1] = 1;
        f = 1;
        nf = 1 - f;
        for (i = 0; i < n; ++i) {
            dp[f][0] = 0;
            for (j = 0; j < m; ++j) {
                dp[f][j + 1] = (obstacleGrid[i][j] == 0 ? dp[nf][j + 1] + dp[f][j] : 0);
            }
            f = 1 - f;
            nf = 1 - f;
        }
        int res = dp[nf][m];
        dp.clear();
        return res;
    }
};
