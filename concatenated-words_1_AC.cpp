// Brute-force DP, from Word Break
// It took me hours on this problem, I tried my best to write a solution with trie.
// But no luck.
#include <algorithm>
#include <string>
#include <unordered_set>
#include <vector>
using std::sort;
using std::string;
using std::unordered_set;
using std::vector;

bool comparator(const string &s1, const string &s2)
{
    return s1.size() < s2.size();
}

class Solution {
public:
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        sort(words.begin(), words.end(), comparator);
        
        vector<string> res;
        unordered_set<string> us;
        int n = words.size();
        int i;
        for (i = 0; i < n; ++i) {
            if (wordBreak(words[i], us)) {
                res.push_back(words[i]);
            } else {
                us.insert(words[i]);
            }
        }
        us.clear();
        
        return res;
    }
private:
    bool wordBreak(const string &w, unordered_set<string> &us) {
        int lw = w.size();
        if (lw == 0 || us.empty()) {
            return false;
        }
        
        vector<bool> dp(lw + 1, false);
        int i, j;
        
        dp[0] = true;
        for (i = 1; i <= lw; ++i) {
            for (j = i - 1; j >= 0; --j) {
                if (dp[j] && us.find(w.substr(j, i - j)) != us.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }
        bool res = dp[lw];
        dp.clear();
        
        return res;
    }
};
