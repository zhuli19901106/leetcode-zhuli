#include <algorithm>
#include <vector>
using std::min;
using std::vector;

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        auto &c = cost;
		int n = c.size();
		vector<int> dp(n + 1, 0);
		dp[0] = dp[1] = 0;
		
		int i;
		for (i = 2; i <= n; ++i) {
			dp[i] = min(dp[i - 1] + c[i - 1], dp[i - 2] + c[i - 2]);
		}
		
		return dp[n];
    }
};
