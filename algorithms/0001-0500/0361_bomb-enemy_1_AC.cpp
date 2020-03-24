// If you know exactly what you're doing, do it right.
// If you don't, think it through.
#include <algorithm>
#include <vector>
using std::max;
using std::vector;

class Solution {
public:
    int maxKilledEnemies(vector<vector<char>>& grid) {
        auto &a = grid;
        int n = a.size();
        int m = (n > 0 ? a[0].size() : 0);
        if (n == 0 || m == 0) {
            return 0;
        }
        
        vector<vector<int>> h(n, vector<int>(m));
        vector<vector<int>> v(n, vector<int>(m));
        
        int i, j;
        int k;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (a[i][j] == 'W') {
                    h[i][j] = 0;
                    continue;
                }
                if (j > 0 && (a[i][j - 1] == '0' || a[i][j - 1] == 'E')) {
                    h[i][j] = h[i][j - 1];
                    continue;
                }
                k = j;
                h[i][j] = 0;
                while (k < m && a[i][k] != 'W') {
                    if (a[i][k] == 'E') {
                        ++h[i][j];
                    }
                    ++k;
                }
            }
        }
        
        for (j = 0; j < m; ++j) {
            for (i = 0; i < n; ++i) {
                if (a[i][j] == 'W') {
                    v[i][j] = 0;
                    continue;
                }
                if (i > 0 && (a[i - 1][j] == '0' || a[i - 1][j] == 'E')) {
                    v[i][j] = v[i - 1][j];
                    continue;
                }
                k = i;
                v[i][j] = 0;
                while (k < n && a[k][j] != 'W') {
                    if (a[k][j] == 'E') {
                        ++v[i][j];
                    }
                    ++k;
                }
            }
        }
        
        int res = 0;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (a[i][j] == '0') {
                    res = max(res, h[i][j] + v[i][j]);
                }
            }
        }
        h.clear();
        v.clear();
        
        return res;
    }
};
