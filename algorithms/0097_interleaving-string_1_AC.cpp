// O(n ^ 2) DP with space optimization
#include <algorithm>
#include <string>
#include <vector>
using std::fill;
using std::sort;
using std::string;
using std::swap;
using std::vector;

class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int n1 = s1.size();
        int n2 = s2.size();
        if (n1 < n2) {
            swap(n1, n2);
            swap(s1, s2);
        }
        
        string ss1 = s1 + s2;
        string ss2 = s3;
        sort(ss1.begin(), ss1.end());
        sort(ss2.begin(), ss2.end());
        if (ss1 != ss2) {
            return false;
        }
        
        vector<vector<bool>> dp(2, vector<bool>(n2 + 1, false));
        int i, j;
        
        dp[0][0] = true;
        for (i = 1; i <= n2; ++i) {
            if (dp[0][i - 1] && s2[i - 1] == s3[i - 1]) {
                dp[0][i] = true;
            }
        }
        
        int f = 1;
        int nf = !f;
        for (i = 1; i <= n1; ++i) {
            fill(dp[f].begin(), dp[f].end(), false);
            if (dp[nf][0] && s1[i - 1] == s3[i - 1]) {
                dp[f][0] = true;
            }
            for (j = 1; j <= n2; ++j) {
                if (dp[nf][j] && s1[i - 1] == s3[i + j - 1]) {
                    dp[f][j] = true;
                }
                if (dp[f][j - 1] && s2[j - 1] == s3[i + j - 1]) {
                    dp[f][j] = true;
                }
            }
            f = !f;
            nf = !f;
        }
        bool res = dp[nf][n2];
        dp.clear();
        
        return res;
    }
};
