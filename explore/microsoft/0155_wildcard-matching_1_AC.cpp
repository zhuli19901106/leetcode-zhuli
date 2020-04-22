// My old backtracking version got TLE, so I turned to DP this time.
class Solution {
public:
    bool isMatch(string s, string p) {
        p = simplify(p);
        int ls = s.size();
        int lp = p.size();
        if (ls == 0) {
            return p == "*" || p == "";
        }
        if (lp == 0) {
            return false;
        }
        
        vector<vector<bool>> dp(ls + 1, vector<bool>(lp + 1, false));
        
        dp[0][0] = true;
        dp[0][1] = (p[0] == '*');
        
        int i, j, k;
        for (i = 1; i <= ls; ++i) {
            for (j = 1; j <= lp; ++j) {
                if (p[j - 1] == '*') {
                    for (k = 0; k <= i; ++k) {
                        if (dp[k][j - 1]) {
                            dp[i][j] = true;
                            break;
                        }
                    }
                } else if (p[j - 1] == '?') {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = (dp[i - 1][j - 1] && (s[i - 1] == p[j - 1]));
                }
            }
        }
        bool res = dp[ls][lp];
        dp.clear();
        
        return res;
    }
private:
    string simplify(string p) {
        string p1 = "";
        int lp = p.size();
        int i = 0;
        while (i < lp) {
            if (p[i] != '*') {
                p1.push_back(p[i++]);
                continue;
            }
            while (i < lp && p[i] == '*') {
                ++i;
            }
            p1.push_back('*');
        }
        
        return p1;
    }
};
