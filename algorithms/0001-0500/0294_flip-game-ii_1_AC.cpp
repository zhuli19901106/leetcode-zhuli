// Sprague-Grundy Theorem, a must-know in game theory.
// Although brute-force searching can pass the test cases, 
// we should learn some math after all.
// https://discuss.leetcode.com/topic/27282/theory-matters-from-backtracking-128ms-to-dp-0ms/2
#include <algorithm>
#include <string>
#include <vector>
using std::max;
using std::string;
using std::vector;

class Solution {
public:
    bool canWin(string s) {
        int ls = s.size();
        int i, j;
        int n = 0;
        vector<int> v;
        
        i = 0;
        while (i < ls) {
            if (s[i] == '-') {
                ++i;
                continue;
            }
            j = i + 1;
            while (j < ls && s[j] == '+') {
                ++j;
            }
            if (j - i >= 2) {
                n = max(n, j - i);
                v.push_back(j - i);
            }
            i = j;
        }
        
        vector<int> dp(n + 1, 0);
        unordered_set<int> us;
        for (i = 2; i <= n; ++i) {
            for (j = 0; j <= i - 2 - j; ++j) {
                us.insert(dp[j] ^ dp[i - 2 - j]);
            }
            dp[i] = firstMissing(us);
            us.clear();
        }
        
        int sum = 0;
        for (auto &val: v) {
            sum ^= dp[val];
        }
        bool res = (sum != 0);
        
        v.clear();
        dp.clear();
        return res;
    }
private:
    int firstMissing(unordered_set<int> &us) {
        int n = us.size();
        int i;
        for (i = 0; i < n; ++i) {
            if (us.find(i) == us.end()) {
                return i;
            }
        }
        return n;
    }
};
