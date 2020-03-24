#include <algorithm>
#include <vector>
using std::max;
using std::vector;

class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = n > 0 ? grid[0].size() : 0;
        if (n == 0 || m == 0) {
            return 0;
        }
        
        vector<int> dj(n * m), sz(n * m);
        int nm = n * m;
        int i;
        for (i = 0; i < n * m; ++i) {
            dj[i] = i;
            sz[i] = 1;
        }
        
        int j;
        int r1, r2;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (i > 0 && grid[i - 1][j] == grid[i][j]) {
                    r1 = findRoot(dj, (i - 1) * m + j);
                    r2 = findRoot(dj, i * m + j);
                    if (r1 != r2) {
                        dj[r2] = r1;
                        sz[r1] += sz[r2];
                    }
                }
                
                if (j > 0 && grid[i][j - 1] == grid[i][j]) {
                    r1 = findRoot(dj, i * m + (j - 1));
                    r2 = findRoot(dj, i * m + j);
                    if (r1 != r2) {
                        dj[r2] = r1;
                        sz[r1] += sz[r2];
                    }
                }
            }
        }
        
        int res = 0;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (grid[i][j] == 1) {
                    res = max(res, sz[findRoot(dj, i * m + j)]);
                }
            }
        }
        
        return res;
    }
private:
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
