#include <algorithm>
#include <string>
#include <vector>
using std::min;
using std::string;
using std::vector;

class Solution {
public:
    int minCut(string s) {
        int ls = s.size();
        if (ls < 2) {
            return 0;
        }
        vector<vector<bool>> p(ls, vector<bool>(ls, false));
        vector<int> dp(ls);
        
        int i, j;
        for (i = 0; i < ls; ++i) {
            p[i][i] = true;
        }
        for (i = 0; i + 1 < ls; ++i) {
            p[i][i + 1] = (s[i] == s[i + 1]);
        }
        for (i = 2; i < ls; ++i) {
            for (j = 0; j + i < ls; ++j) {
                if (s[j] == s[j + i] && p[j + 1][j + i - 1]) {
                    p[j][j + i] = true;
                }
            }
        }
        
        for (i = 0; i < ls; ++i) {
            if (p[0][i]) {
                dp[i] = 1;
                continue;
            }
            dp[i] = i + 1;
            for (j = i; j > 0; --j) {
                if (p[j][i]) {
                    dp[i] = min(dp[i], dp[j - 1] + 1);
                }
            }
        }
        int res = dp[ls - 1] - 1;
        p.clear();
        dp.clear();
        
        return res;
    }
};
