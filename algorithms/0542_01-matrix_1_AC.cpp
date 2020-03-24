// BFS
#include <unordered_set>
#include <vector>
using std::unordered_set;
using std::vector;

static const int offset[4][2] = {{-1, 0}, {+1, 0}, {0, -1}, {0, +1}};

class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        auto &a = matrix;
        int n = a.size();
        int m = (n > 0 ? a[0].size() : 0);
        if (n == 0 || m == 0) {
            return a;
        }
        
        vector<vector<int>> res(n, vector<int>(m, -1));
        vector<unordered_set<int>> v(2);
        int i, j;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (a[i][j] == 0) {
                    v[0].insert(i * m + j);
                }
            }
        }
        
        int cc = n * m;
        int d = 0;
        int nf = 0;
        int f = !nf;
        
        int k;
        int i1, j1;
        while (true) {
            for (const int &val: v[nf]) {
                i = val / m;
                j = val % m;
                res[i][j] = d;
                --cc;
            }
            if (cc <= 0) {
                break;
            }
            
            for (const int &val: v[nf]) {
                i = val / m;
                j = val % m;
                for (k = 0; k < 4; ++k) {
                    i1 = i + offset[k][0];
                    j1 = j + offset[k][1];
                    if (i1 < 0 || i1 > n - 1 || j1 < 0 || j1 > m - 1) {
                        continue;
                    }
                    if (res[i1][j1] != -1) {
                        continue;
                    }
                    v[f].insert(i1 * m + j1);
                }
            }
            
            ++d;
            f = !f;
            nf = !f;
            v[f].clear();
        }
        v.clear();
        
        return res;
    }
};
