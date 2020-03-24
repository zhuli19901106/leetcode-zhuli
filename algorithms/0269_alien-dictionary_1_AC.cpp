// Topological sort
// Number of nodes is too small, so don't bother with heap optimization.
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using std::make_pair;
using std::pair;
using std::string;
using std::unordered_map;
using std::unordered_set;
using std::vector;

class Solution {
public:
    string alienOrder(vector<string>& words) {
        auto &w = words;
        int n = w.size();
        
        unordered_map<char, unordered_set<char>> g;
        unordered_map<char, int> ind;
        
        for (auto &s: w) {
            for (auto &ch: s) {
                g[ch];
                ind[ch] = 0;
            }
        }
        int m = ind.size();
        
        int ls, lt;
        int i, j;
        for (i = 0; i + 1 < n; ++i) {
            string &s = w[i];
            string &t = w[i + 1];
            ls = s.size();
            lt = t.size();
            for (j = 0; j < ls && j < lt; ++j) {
                if (s[j] == t[j]) {
                    continue;
                }
                if (g[s[j]].find(t[j]) == g[s[j]].end()) {
                    g[s[j]].insert(t[j]);
                    ++ind[t[j]];
                }
                break;
            }
        }
        
        char ch;
        string res = "";
        while (true) {
            ch = '\0';
            for (auto &p: ind) {
                if (p.second == 0) {
                    ch = p.first;
                    break;
                }
            }
            if (ch == '\0') {
                break;
            }
            for (auto &ch1: g[ch]) {
                --ind[ch1];
            }
            g.erase(ch);
            ind.erase(ch);
            
            res.push_back(ch);
            --m;
        }
        if (m > 0) {
            res = "";
        }
        g.clear();
        ind.clear();
        
        return res;
    }
};
