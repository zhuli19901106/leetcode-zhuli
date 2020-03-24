// When searching slows down, it's time to do some pruning.
// Try DP with this problem.
// When the string is long enough, there can be collisions.
#include <algorithm>
#include <cstdint>
#include <string>
#include <unordered_map>
#include <vector>
using std::max;
using std::min;
using std::string;
using std::unordered_map;
using std::vector;

class Solution {
public:
    Solution() {
        pw.push_back(1);
    }
    
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        vector<string> res;
        auto &wd = wordDict;
        int nw = wd.size();
        if (nw == 0) {
            return res;
        }
        
        calcHash(s, hs);
        
        int i, j;
        int64_t hw;
        int lw;
        
        min_lw = max_lw = wd[0].size();
        for (i = 0; i < nw; ++i) {
            hw = 0;
            lw = wd[i].size();
            min_lw = min(min_lw, lw);
            max_lw = max(max_lw, lw);
            for (j = 0; j < lw; ++j) {
                hw = hw * P + (wd[i][j] - 'a' + 1);
            }
            um[hw] = wd[i];
        }
        
        wordBreakDP(s, wd);
        dfs(0, s, res);
        
        dp.clear();
        hs.clear();
        vs.clear();
        um.clear();
        
        return res;
    }
    
    ~Solution() {
        pw.clear();
    }
private:
    static const int64_t P = 31;
    vector<int64_t> pw;
    
    vector<vector<bool>> dp;
    vector<int64_t> hs;
    vector<string> vs;
    unordered_map<int64_t, string> um;
    
    int min_lw;
    int max_lw;
    
    void wordBreakDP(const string &s, vector<string> &wd) {
        int ls = s.size();
        dp.resize(ls, vector<bool>(ls, false));
        int i, j, k;
        int64_t hw;
        for (i = 0; i < ls; ++i) {
            for (j = i; j < ls; ++j) {
                hw = hash(hs, i + 1, j + 1);
                if (um.find(hw) != um.end()) {
                    dp[i][j] = true;
                }
                for (k = i; k + 1 <= j; ++k) {
                    hw = hash(hs, k + 2, j + 1);
                    if (dp[i][k] && um.find(hw) != um.end()) {
                        dp[i][j] = true;
                        break;
                    }
                }
            }
        }
    }
    
    int64_t getPow(int i) {
        while (pw.size() <= i) {
            pw.push_back(pw.back() * P);
        }
        return pw[i];
    }
    
    void calcHash(const string &s, vector<int64_t> &h) {
        int ls = s.size();
        h.resize(ls + 2, 0);
        int i;
        for (i = 1; i <= ls; ++i) {
            h[i] = h[i - 1] * P + (s[i - 1] - 'a' + 1);
        }
    }
    
    int64_t hash(vector<int64_t> &h, int left, int right) {
        return h[right] - h[left - 1] * getPow(right - left + 1);
    }
    
    void dfs(int idx, const string &s, vector<string> &res) {
        int ls = s.size();
        if (idx == ls) {
            string ss = "";
            int n = vs.size();
            int i;
            for (i = 0; i < n; ++i) {
                ss += vs[i];
                ss.push_back(' ');
            }
            ss.pop_back();
            res.push_back(ss);
            
            return;
        }
        if (!dp[idx][ls - 1]) {
            // The rest can't be broken into valid words.
            return;
        }
        
        string w = "";
        int64_t hw;
        int i;
        int lw;
        for (i = idx; i < ls; ++i) {
            w.push_back(s[i]);
            lw = w.size();
            if (lw < min_lw) {
                continue;
            }
            if (lw > max_lw) {
                break;
            }
            hw = hash(hs, idx + 1, i + 1);
            if (um.find(hw) == um.end()) {
                continue;
            }
            string &w1 = um[hw];
            if (w.size() != w1.size() || w != w1) {
                continue;
            }
            
            vs.push_back(w);
            dfs(i + 1, s, res);
            vs.pop_back();
        }
    }
};
