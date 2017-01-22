// If it's about games, always try DP before DFS.
// It's not important whether the algorithm is intuitive or not.
// What matters is that you stay cool and reason carefully.
#include <algorithm>
using std::min;

class Solution {
public:
    bool PredictTheWinner(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) {
            return true;
        }
        vector<int> sum(n + 1, 0);
        int i;
        for (i = 0; i < n; ++i) {
            sum[i + 1] = sum[i] + nums[i];
        }
        
        vector<vector<int>> dp(n, vector<int>(n, 0));
        int j;
        for (i = 0; i < n; ++i) {
            dp[i][i] = nums[i];
        }
        int s1, s2;
        for (i = 1; i < n; ++i) {
            for (j = 0; j + i < n; ++j) {
                s1 = nums[j] + (sum[j + i + 1] - sum[j + 1]) - dp[j + 1][j + i];
                s2 = nums[j + i] + (sum[j + i] - sum[j]) - dp[j][j + i - 1];
                dp[j][j + i] = max(s1, s2);
            }
        }
        bool can_win = dp[0][n - 1] >= sum[n] - dp[0][n - 1];
        dp.clear();
        sum.clear();
        
        return can_win;
    }
};
