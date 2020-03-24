// Topological sort
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using std::max;
using std::unordered_map;
using std::unordered_set;
using std::vector;

class Solution {
public:
    bool sequenceReconstruction(vector<int>& org, vector<vector<int>>& seqs) {
        int n = org.size();
        int max_val = 0;
        for (auto &s: seqs) {
            for (auto &val: s) {
                if (val < 1 || val > n) {
                    return false;
                }
                max_val = max(max_val, val);
            }
        }
        if (max_val != n) {
            return false;
        }
        
        bool suc = true;
        
        unordered_map<int, unordered_set<int>> g;
        unordered_map<int, unordered_set<int>> mm;
        vector<int> ind(n + 1, 0);
        
        int ls;
        int i;
        int x, y;
        for (i = 1; i <= n; ++i) {
            mm[0].insert(i);
        }
        for (auto &s: seqs) {
            ls = s.size();
            for (i = 0; i + 1 < ls; ++i) {
                x = s[i];
                y = s[i + 1];
                if (g[x].find(y) != g[x].end()) {
                    continue;
                }
                g[x].insert(y);
                inc(mm, ind, y);
            }
        }
        
        int lo = org.size();
        i = 0;
        while (i < lo) {
            if (mm[0].size() != 1 || (x = *(mm[0].begin())) != org[i]) {
                suc = false;
                break;
            }
            ++i;
            mm[0].erase(x);
            for (auto it = g[x].begin(); it != g[x].end(); ++it) {
                y = *it;
                dec(mm, ind, y);
            }
            g[x].clear();
            g.erase(x);
        }
        
        g.clear();
        mm.clear();
        ind.clear();
        
        return suc;
    }
private:
    void inc(unordered_map<int, unordered_set<int>> &mm, vector<int> &ind, 
        int i) {
        int val = ind[i]++;
        mm[val].erase(i);
        mm[val + 1].insert(i);
    }
    
    void dec(unordered_map<int, unordered_set<int>> &mm, vector<int> &ind, 
        int i) {
        int val = ind[i]--;
        mm[val].erase(i);
        mm[val - 1].insert(i);
    }
};
