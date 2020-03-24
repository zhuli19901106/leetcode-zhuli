#include <string>
#include <vector>
using std::string;
using std::vector;

class Solution {
public:
    int minDistance(string word1, string word2) {
        return word1.size() + word2.size() - 2 * LCS(word1, word2);
    }
private:
    int LCS(const string &s1, const string &s2) {
        int ls1 = s1.size();
        int ls2 = s2.size();
        if (ls1 == 0 || ls2 == 0) {
            return 0;
        }
        if (ls1 < ls2) {
            return LCS(s2, s1);
        }
        
        vector<vector<int>> dp(2, vector<int>(ls2 + 1, 0));
        int f, nf;
        int i, j;
        
        f = 0;
        nf = !f;
        for (i = 1; i <= ls1; ++i) {
            dp[f][0] = 0;
            for (j = 1; j <= ls2; ++j) {
                if (s1[i - 1] == s2[j - 1]) {
                    dp[f][j] = dp[nf][j - 1] + 1;
                } else {
                    dp[f][j] = max(dp[f][j - 1], dp[nf][j]);
                }
            }
            f = !f;
            nf = !f;
        }
        int res = dp[nf][ls2];
        dp.clear();
        
        return res;
    }
};
