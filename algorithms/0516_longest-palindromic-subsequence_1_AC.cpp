// Traditional DP
#include <algorithm>
#include <string>
using std::string;

class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int ls = s.size();
        if (ls < 2) {
            return ls;
        }
        
        vector<vector<int>> dp(ls, vector<int>(ls, 0));
        int i, j;
        for (i = 0; i < ls; ++i) {
            dp[i][i] = 1;
        }
        for (i = 0; i + 1 < ls; ++i) {
            dp[i][i + 1] = (s[i] == s[i + 1]) ? 2 : 1;
        }
        for (i = 2; i < ls; ++i) {
            for (j = 0; j + i < ls; ++j) {
                if (s[j] == s[j + i]) {
                    dp[j][j + i] = dp[j + 1][j + i - 1] + 2;
                } else {
                    dp[j][j + i] = max(dp[j][j + i - 1], dp[j + 1][j + i]);
                }
            }
        }
        int res = dp[0][ls - 1];
        dp.clear();
        
        return res;
    }
};
