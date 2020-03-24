#include <algorithm>
#include <vector>
using std::min;
using std::vector;

class Solution {
public:
    int minimumDeleteSum(string s1, string s2) {
        int ls1 = s1.size();
        int ls2 = s2.size();
        vector<vector<int>> dp(ls1 + 1, vector<int>(ls2 + 1, 0));
        
        int i, j;
        for (i = 1; i <= ls1; ++i) {
            dp[i][0] = dp[i - 1][0] + s1[i - 1];
        }
        for (j = 1; j <= ls2; ++j) {
            dp[0][j] = dp[0][j - 1] + s2[j - 1];
        }
        for (i = 1; i <= ls1; ++i) {
            for (j = 1; j <= ls2; ++j) {
                if (s1[i - 1] == s2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = min(dp[i - 1][j] + s1[i - 1], dp[i][j - 1] + s2[j - 1]);
                }
            }
        }
        int res = dp[ls1][ls2];
        dp.clear();
        
        return res;
    }
};
