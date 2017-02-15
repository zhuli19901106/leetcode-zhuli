// Direction matters
#include <algorithm>
#include <cstdint>
#include <vector>
using std::max;
using std::min;
using std::vector;

class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        auto &a = dungeon;
        int n = a.size();
        int m = n > 0 ? a[0].size() : 0;
        if (n == 0 || m == 0) {
            return 1;
        }
        
        int i, j;
        vector<vector<int>> dp(n, vector<int>(m, 0));
        dp[n - 1][m - 1] = max(1, 1 - a[n - 1][m - 1]);
        for (i = n - 2; i >= 0; --i) {
            dp[i][m - 1] = max(1, dp[i + 1][m - 1] - a[i][m - 1]);
        }
        for (j = m - 2; j >= 0; --j) {
            dp[n - 1][j] = max(1, dp[n - 1][j + 1] - a[n - 1][j]);
        }
        for (i = n - 2; i >= 0; --i) {
            for (j = m - 2; j >= 0; --j) {
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - a[i][j]);
            }
        }
        int res = dp[0][0];
        dp.clear();
        
        return res;
    }
};
