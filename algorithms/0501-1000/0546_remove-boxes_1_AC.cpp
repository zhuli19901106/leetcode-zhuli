// A clever DP solution.
// https://discuss.leetcode.com/topic/84687/java-top-down-and-bottom-up-dp-solutions
#include <algorithm>
#include <cstdint>
#include <vector>
using std::max;
using std::vector;

class Solution {
public:
    int removeBoxes(vector<int>& boxes) {
        auto &a = boxes;
        int n = a.size();
        if (n == 0) {
            return 0;
        }
        
        vector<vector<vector<int16_t>>> dp(n, 
            vector<vector<int16_t>>(n, vector<int16_t>(n, 0)));
        
        int i, j;
        for (i = 0; i < n; ++i) {
            for (j = 0; j <= i; ++j) {
                dp[i][i][j] = (j + 1) * (j + 1);
            }
        }
        
        int k;
        int ii, jj;
        int res;
        for (i = 1; i < n; ++i) {
            for (j = 0; j + i < n; ++j) {
                k = j + i;
                for (ii = 0; ii <= j; ++ii) {
                    res = (ii + 1) * (ii + 1) + dp[j + 1][k][0];
                    for (jj = j + 1; jj <= k; ++jj) {
                        if (a[j] == a[jj]) {
                            res = max(res, dp[j + 1][jj - 1][0] + dp[jj][k][ii + 1]);
                        }
                    }
                    dp[j][k][ii] = res;
                }
            }
        }
        
        res = dp[0][n - 1][0];
        dp.clear();
        
        return res;
    }
};
