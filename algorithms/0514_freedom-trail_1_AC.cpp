// Traditional DP
// The space can be optimized to O(N), don't wanna bother.
#include <algorithm>
#include <climits>
#include <cmath>
#include <string>
#include <vector>
using std::abs;
using std::min;
using std::string;
using std::vector;

class Solution {
public:
    int findRotateSteps(string ring, string key) {
        int lr = ring.size();
        int lk = key.size();
        if (lk == 0) {
            return 0;
        }
        
        vector<vector<int>> dp(lk, vector<int>(lr, INT_MAX));
        
        int i, j, k;
        int d;
        
        j = 0;
        for (i = 0; i < lr; ++i) {
            if (ring[i] != key[0]) {
                continue;
            }
            d = abs(i - j);
            dp[0][i] = min(d, lr - d) + 1;
        }
        
        for (i = 1; i < lk; ++i) {
            for (j = 0; j < lr; ++j) {
                if (ring[j] != key[i]) {
                    continue;
                }
                for (k = 0; k <  lr; ++k) {
                    if (ring[k] != key[i - 1]) {
                        continue;
                    }
                    d = abs(j - k);
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + min(d, lr - d) + 1);
                }
            }
        }
        
        int res = INT_MAX;
        for (i = 0; i < lr; ++i) {
            res = min(res, dp[lk - 1][i]);
        }
        dp.clear();
        
        return res;
    }
};
