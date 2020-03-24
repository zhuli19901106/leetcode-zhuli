// Brute-force DP
// I think there must be some more graceful solution.
#include <algorithm>
#include <string>
#include <vector>
using std::sort;
using std::string;
using std::vector;

class Solution {
public:
    bool isScramble(string s1, string s2) {
        int n = s1.size();
        if (n != s2.size()) {
            return false;
        }
        
        vector<vector<vector<bool>>> dp;
        dp.resize(n, vector<vector<bool>>(n, vector<bool>(n, false)));
        
        int i, j;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < n; ++j) {
                if (s1[i] == s2[j]) {
                    dp[i][i][j] = true;
                }
            }
        }
        
        int k, ii;
        for (i = 1; i < n; ++i) {
            for (j = 0; j + i < n; ++j) {
                for (k = 0; k + i < n; ++k) {
                    if (dp[j][j + i][k]) {
                        continue;
                    }
                    for (ii = 0; ii < i; ++ii) {
                        if (dp[j][j + ii][k] && dp[j + ii + 1][j + i][k + ii + 1]) {
                            // left -> left;
                            // right -> right;
                            dp[j][j + i][k] = true;
                            break;
                        }
                        if (dp[j][j + ii][k + i - ii] && dp[j + ii + 1][j + i][k]) {
                            // left -> right;
                            // right -> left;
                            dp[j][j + i][k] = true;
                        }
                    }
                }
            }
        }
        bool res = dp[0][n - 1][0];
        dp.clear();
        
        return res;
    }
};
