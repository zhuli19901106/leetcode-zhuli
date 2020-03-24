// DFS + Memorization
#include <algorithm>
#include <vector>
using std::max;
using std::vector;

class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) {
            return 0;
        }
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        int i;
        dfs(0, n - 1, nums, dp, 1, 1);
        
        int res = dp[0][n - 1];
        dp.clear();
        return res;
    }
private:
    int getDP(int i, int j, vector<vector<int>> &dp) {
        return i <= j ? dp[i][j] : 0;
    }
    
    void dfs(int i, int j, vector<int> &nums, vector<vector<int>> &dp, 
        int ll, int rr) {
        if (dp[i][j] != 0) {
            return;
        }
        if (i == j) {
            dp[i][j] = ll * nums[i] * rr;
            return;
        }
        
        int res = 0;
        int k;
        int s1, s2;
        for (k = i; k <= j; ++k) {
            if (i <= k - 1 && dp[i][k - 1] == 0) {
                dfs(i, k - 1, nums, dp, ll, nums[k]);
            }
            s1 = getDP(i, k - 1, dp);
            if (k + 1 <= j && dp[k + 1][j] == 0) {
                dfs(k + 1, j, nums, dp, nums[k], rr);
            }
            s2 = getDP(k + 1, j, dp);
            res = max(res, s1 + s2 + ll * nums[k] * rr);
        }
        dp[i][j] = res;
    }
};
