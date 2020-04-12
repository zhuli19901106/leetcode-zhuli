// Since the word length is short enough, we can use hash values to simulate a trie.
#include <algorithm>
#include <string>
#include <unordered_set>
#include <vector>
using std::reverse;
using std::string;
using std::unordered_set;
using std::vector;

class Solution {
public:
    vector<vector<string>> wordSquares(vector<string>& words) {
        vector<vector<string>> res;
        auto &w = words;
        int nw = w.size();
        if (nw == 0) {
            return res;
        }
        int lw = w[0].size();
        
        unordered_set<int> us;
        int val;
        int i, j;
        for (i = 0; i < nw; ++i) {
            val = 0;
            for (j = 0; j < lw; ++j) {
                val = val * 27 + (w[i][j] - 'a' + 1);
                us.insert(val);
            }
        }
        
        // v[i] is the hash value for i-th row.
        vector<int> v(lw, 0);
        dfs(0, 0, v, lw, us, res);
        us.clear();
        
        return res;
    }
private:
    void dfs(int x, int y, vector<int> &v, int lw, unordered_set<int> &us, 
        vector<vector<string>> &res) {
        int i;
        if (x == lw && y == lw) {
            res.push_back(vector<string>());
            auto &rb = res.back();
            for (i = 0; i < lw; ++i) {
                rb.push_back(hashToWord(v[i]));
            }
            return;
        }
        
        int old_vx = v[x];
        int old_vy;
        int vx;
        int vy;
        for (i = 1; i <= 26; ++i) {
            vx = v[x] * 27 + i;
            if (us.find(vx) == us.end()) {
                continue;
            }
            old_vy = v[y];
            if (y > x) {
                vy = v[y] * 27 + i;
                if (us.find(vy) == us.end()) {
                    continue;
                }
            } else {
                vy = vx;
            }
            
            v[x] = vx;
            v[y] = vy;
            if (y + 1 < lw) {
                dfs(x, y + 1, v, lw, us, res);
            } else {
                dfs(x + 1, x + 1, v, lw, us, res);
            }
            v[y] = old_vy;
            v[x] = old_vx;
        }
    }
    
    string hashToWord(int val) {
        string s = "";
        while (val > 0) {
            s.push_back('a' + val % 27 - 1);
            val /= 27;
        }
        reverse(s.begin(), s.end());
        
        return s;
    }
};
