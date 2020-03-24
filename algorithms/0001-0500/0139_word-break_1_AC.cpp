#include <unordered_set>
using std::unordered_set;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict;
        for (auto it = wordDict.begin(); it != wordDict.end(); ++it) {
            dict.insert(*it);
        }
        
        int ls = s.size();
        int i, j;
        vector<bool> dp(ls + 1, false);
        dp[0] = true;
        for (i = 1; i <= ls; ++i) {
            for (j = 0; !dp[i] && j < i; ++j) {
                if (dp[j] && dict.find(s.substr(j, i - j)) != dict.end()) {
                    dp[i] = true;
                }
            }
        }
        bool res = dp[ls];
        dp.clear();
        return res;
    }
};
