// Levenshtein distance
#include <algorithm>
#include <climits>
using std::fill;
using std::swap;

class Solution {
public:
    int minDistance(string word1, string word2) {
        auto &s1 = word1;
        auto &s2 = word2;
        int n1 = s1.size();
        int n2 = s2.size();
        if (n1 < n2) {
            swap(n1, n2);
            swap(s1, s2);
        }
        vector<vector<int>> dp(2, vector<int>(n2 + 1));
        
        int i, j;
        for (i = 0; i <= n2; ++i) {
            dp[0][i] = i;
        }
        
        int f = 1;
        int nf = !f;
        for (i = 1; i <= n1; ++i) {
            fill(dp[f].begin(), dp[f].end(), INT_MAX);
            dp[f][0] = i;
            for (j = 1; j <= n2; ++j) {
                if (s1[i - 1] == s2[j - 1]) {
                    dp[f][j] = dp[nf][j - 1];
                } else {
                    dp[f][j] = min(dp[nf][j], dp[f][j - 1]) + 1;
                    dp[f][j] = min(dp[f][j], dp[nf][j - 1] + 1);
                }
            }
            f = !f;
            nf = !f;
        }
        int res = dp[nf][n2];
        dp.clear();
        
        return res;
    }
};
