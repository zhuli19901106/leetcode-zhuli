// Actually k can be as large as O(n ^ 2).
// Do some reduction before coding.
// Try not to worry about boundary, it simplifies the problem.
#include <algorithm>
#include <vector>
using std::max;
using std::min;
using std::vector;

class Solution {
public:
    int kInversePairs(int n, int iv) {
        if (iv == 0) {
            return 1;
        }
        
        const int MOD = 1000000007;
        vector<vector<int>> dp(2, vector<int>(iv + 1));
        int m, m0;
        int i, j;
        int f, nf;
        
        f = 1;
        nf = !f;
        dp[nf][0] = 1;
        m0 = 0;
        for (i = 1; i < n; ++i) {
            m = min(i * (i + 1) / 2, iv);
            for (j = 0; j <= m; ++j) {
                dp[f][j] = 0;
            }
            
            dp[f][0] = 1;
            for (j = 1; j <= m; ++j) {
                dp[f][j] = dp[f][j - 1];
                if (j <= m0) {
                    dp[f][j] = (dp[f][j] + dp[nf][j]) % MOD;
                }
                if (j - (i + 1) >= 0 && j - (i + 1) <= m0) {
                    dp[f][j] = (dp[f][j] + MOD - dp[nf][j - (i + 1)]) % MOD;
                }
            }
            m0 = m;
            
            f = !f;
            nf = !f;
        }
        
        int res = dp[nf][iv];
        dp.clear();
        
        return res;
    }
};
