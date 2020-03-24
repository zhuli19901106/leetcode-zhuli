#include <string>
#include <unordered_map>
#include <vector>
using std::string;
using std::to_string;
using std::unordered_map;
using std::vector;

class Solution {
public:
    string encode(string s) {
        int ls = s.size();
        if (ls <= 4) {
            return s;
        }
        
        vector<int> next(ls + 1);
        vector<vector<int>> dp(ls, vector<int>(ls));
        
        // Calculate the minimum length of repetend for s[i...j].
        int i, j;
        for (i = 0; i < ls; ++i) {
            calcNext(s, i, next);
            for (j = 1; j <= ls - i; ++j) {
                if (j % (j - next[j]) == 0) {
                    // A repetend is detected
                    dp[i][i + j - 1] = j - next[j];
                } else {
                    dp[i][i + j - 1] = j;
                }
            }
        }
        
        unordered_map<int, string> um;
        // After thinking for a long time, I still couldn't figure out a loop style DP solution.
        // So let's search.
        dfs(0, ls - 1, s, dp, um);
        dp.clear();
        next.clear();
        
        string res = um[ls - 1];
        um.clear();
        
        return res;
    }
private:
    void dfs(int i, int j, const string &s, vector<vector<int>> &dp, 
        unordered_map<int, string> &um) {
        int ls = s.size();
        if (um.find(i * ls + j) != um.end()) {
            return;
        }
        
        if (j - i + 1 <= 4) {
            um[i * ls + j] = s.substr(i, j - i + 1);
            return;
        }
        
        int k;
        if (dp[i][j] < j - i + 1) {
            k = i + dp[i][j] - 1;
            dfs(i, k, s, dp, um);
            string ss = um[i * ls + k];
            string sd = to_string((j - i + 1) / dp[i][j]);
            
            if (sd.size() + ss.size() + 2 < j - i + 1) {
                um[i * ls + j] = sd + "[" + ss + "]";
            } else {
                um[i * ls + j] = s.substr(i, j - i + 1);
            }
            return;
        }
        
        string res = s.substr(i, j - i + 1);
        for (k = i; k < j; ++k) {
            dfs(i, k, s, dp, um);
            dfs(k + 1, j, s, dp, um);
            string &s1 = um[i * ls + k];
            string &s2 = um[(k + 1) * ls + j];
            if (s1.size() + s2.size() < res.size()) {
                res = s1 + s2;
            }
        }
        um[i * ls + j] = res;
    }
    
    void calcNext(const string &s, int idx, vector<int> &next) {
        int i, j;
        int ls = s.size();
        
        i = 0;
        j = -1;
        next[i] = j;
        while (i + idx < ls) {
            if (j == -1 || s[i + idx] == s[j + idx]) {
                next[++i] = ++j;
            } else {
                j = next[j];
            }
        }
    }
};
