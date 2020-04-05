// Manacher Algorithm
// A clever application of DP.
class Solution {
public:
    string longestPalindrome(string s) {
        int ls = s.size();
        if (ls < 2) {
            return s;
        }
        string ss = fillChars(s);
        ls = ss.size();
        vector<int> dp(ls, 1);
        
        int i, j;
        int ci = 0;
        int far_pos = 0;
        for (i = 1; i < ls; ++i) {
            // The key is here
            if (far_pos < i) {
                j = 1;
            } else {
                j = min(far_pos - i + 1, dp[2 * ci - i]);
            }
            while (i - j >= 0 && i + j <= ls - 1 && ss[i - j] == ss[i + j]) {
                ++j;
            }
            dp[i] = j;
            if (i + dp[i] - 1 > far_pos) {
                ci = i;
                far_pos = i + dp[i] - 1;
            }
        }
        
        string res = "";
        int max_len = 0;
        
        int len;
        for (i = 0; i < ls; i += 2) {
            len = (dp[i] & ~1);
            if (len > max_len) {
                max_len = len;
                j = (i - len >> 1);
                res = s.substr(j, max_len);
            }
        }
        for (i = 1; i < ls; i += 2) {
            len = (dp[i] - 1 & ~1) + 1;
            if (len > max_len) {
                max_len = len;
                j = (i - len >> 1);
                res = s.substr(j, max_len);
            }
        }
        
        dp.clear();
        return res;
    }
private:
    static const char UNUSED_CHAR_HEAD = 1;
    static const char UNUSED_CHAR = 2;
    
    // Fill the string with unused chars, 
    // so that every palindromic substring has odd length.
    string fillChars(string s) {
        string res;
        int ls = s.size();
        
        int i;
        res.push_back(UNUSED_CHAR_HEAD);
        for (i = 0; i < ls; ++i) {
            res.push_back(s[i]);
            res.push_back(UNUSED_CHAR);
        }
        return res;
    }
};
