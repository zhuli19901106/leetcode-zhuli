// DFS + backtracking
// I think it can be further accelerated with string hashing.
#include <string>
#include <unordered_map>
#include <unordered_set>
using std::string;
using std::unordered_map;
using std::unordered_set;

class Solution {
public:
    bool wordPatternMatch(string pattern, string str) {
        p = pattern;
        s = str;
        lp = p.size();
        ls = s.size();
        
        int i, j;
        string t;
        for (i = 0; i < ls; ++i) {
            for (j = i; j < ls; ++j) {
                t.push_back(s[j]);
                um[t].insert(i);
            }
            t.clear();
        }
        
        for (i = 0; i < lp; ++i) {
            ++mc[p[i]];
        }
        
        bool res = dfs(0, 0, 0);
        um.clear();
        ms.clear();
        mp.clear();
        mc.clear();
        return res;
    }
private:
    unordered_map<string, unordered_set<int>> um;
    unordered_map<char, string> ms;
    unordered_map<string, char> mp;
    unordered_map<char, int> mc;
    
    string p;
    string s;
    int lp;
    int ls;
    
    bool dfs(int si, int pi, int sum) {
        if (si == ls) {
            return pi == lp;
        }
        if (pi == lp) {
            return si == ls;
        }
        
        char c = p[pi];
        string ss;
        if (ms.find(c) != ms.end()) {
            ss = ms[c];
            if (um[ss].find(si) == um[ss].end()) {
                return false;
            }
            return dfs(si + ss.size(), pi + 1, sum);
        } else {
            int i;
            ss = "";
            for (i = si; i < ls; ++i) {
                ss.push_back(s[i]);
                if (sum + mc[c] * ss.size() > ls) {
                    return false;
                }
                if (ms.size() + 1 == mc.size() && sum + mc[c] * ss.size() != ls) {
                    continue;
                }
                if (mp.find(ss) != mp.end()) {
                    continue;
                }
                
                ms[c] = ss;
                mp[ss] = c;
                if (dfs(si + ss.size(), pi + 1, sum + mc[c] * ss.size())) {
                    return true;
                }
                mp.erase(ss);
                ms.erase(c);
            }
            return false;
        }
    }
};
