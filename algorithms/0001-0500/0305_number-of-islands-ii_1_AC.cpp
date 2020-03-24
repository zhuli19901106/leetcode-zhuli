// Ammortizedly O(k) solution with union-find set.
#include <unordered_set>
#include <utility>
#include <vector>
using std::make_pair;
using std::pair;
using std::unordered_set;
using std::vector;

static const int offset[4][2] = {{-1, 0}, {+1, 0}, {0, -1}, {0, +1}};

class Solution {
public:
    vector<int> numIslands2(int m, int n, vector<pair<int, int>>& positions) {
        swap(m, n);
        
        vector<bool> a(n * m, false);
        vector<int> dj(n * m);
        int i, j;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                dj[i * m + j] = i * m + j;
            }
        }
        
        int cnt = 0;
        int k;
        int i1, j1;
        int ri, rj;
        unordered_set<int> us;
        vector<int> res;
        for (auto &p: positions) {
            i = p.first;
            j = p.second;
            if (!inbound(i, j, n, m) || a[i * m + j]) {
                res.push_back(cnt);
                continue;
            }
            
            for (k = 0; k < 4; ++k) {
                i1 = i + offset[k][0];
                j1 = j + offset[k][1];
                if (inbound(i1, j1, n, m) && a[i1 * m + j1]) {
                    us.insert(findRoot(dj, i1 * m + j1));
                }
            }
            
            for (auto &val: us) {
                dj[val] = i * m + j;
            }
            a[i * m + j] = true;
            
            cnt += (1 - us.size());
            res.push_back(cnt);
            us.clear();
        }
        a.clear();
        dj.clear();
        
        return res;
    }
private:
    inline bool inbound(int x, int y, int n, int m) {
        return x >= 0 && x <= n - 1 && y >= 0 && y <= m - 1;
    }
    
    int findRoot(vector<int> &dj, int x) {
        int r = x;
        while (r != dj[r]) {
            r = dj[r];
        }
        int k = x;
        while (x != r) {
            x = dj[x];
            dj[k] = r;
            k = x;
        }
        return r;
    }
};
