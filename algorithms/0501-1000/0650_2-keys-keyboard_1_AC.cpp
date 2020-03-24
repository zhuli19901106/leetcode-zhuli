// Trivial
#include <vector>
using std::vector;

class Solution {
public:
    int minSteps(int n) {
        vector<int> dp(n + 1, 0);
        int i;
        for (i = 2; i <= n; ++i) {
            dp[i] = i;
        }
        
        int j;
        for (i = 2; i <= n; ++i) {
            for (j = 1; j <= n / j; ++j) {
                if (i % j != 0) {
                    continue;
                }
                if (dp[i] > dp[j] + i / j) {
                    dp[i] = dp[j] + i / j;
                }
                if (j != i / j && dp[i] > dp[i / j] + j) {
                    dp[i] = dp[i / j] + j;
                }
            }
        }
        
        int res = dp[n];
        return res;
    }
};
