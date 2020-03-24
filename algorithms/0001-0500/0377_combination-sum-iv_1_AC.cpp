// I was surprised that I chose to use DFS.
// How foolish, when the answer is DP.
#include <algorithm>
using std::sort;

class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        if (target <= 0) {
            return 0;
        }
        
        sort(nums.begin(), nums.end());
        vector<int> dp(target + 1, 0);
        
        int n = nums.size();
        int i, j;
        dp[0] = 1;
        for (i = 1; i <= target; ++i) {
            for (j = 0; j < n; ++j) {
                if (nums[j] > i) {
                    break;
                }
                dp[i] += dp[i - nums[j]];
            }
        }
        return dp[target];
    }
};
