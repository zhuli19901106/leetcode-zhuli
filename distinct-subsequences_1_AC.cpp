// Traditional O(n ^ 2) DP
#include <string>
#include <vector>
using std::string;
using std::vector;

class Solution {
public:
    int numDistinct(string s, string t) {
        int ls = s.size();
        int lt = t.size();
        if (ls < lt) {
            return 0;
        }
        
        vector<vector<int>> dp(2, vector<int>(lt + 1, 0));
        dp[0][0] = 1;
        
        int f = 1;
        int nf = !f;
        int i, j;
        for (i = 1; i <= ls; ++i) {
            dp[f][0] = 1;
            for (j = 1; j <= lt; ++j) {
                dp[f][j] = dp[nf][j];
                if (s[i - 1] == t[j - 1]) {
                    dp[f][j] += dp[nf][j - 1];
                }
            }
            f = !f;
            nf = !f;
        }
        int res = dp[nf][lt];
        dp.clear();
        
        return res;
    }
};

