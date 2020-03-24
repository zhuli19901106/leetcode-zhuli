#include <utility>
using std::make_pair;

static const int dir[4][2] = {{-1, 0}, {+1, 0}, {0, -1}, {0, +1}};

class Solution {
public:
    vector<pair<int, int>> pacificAtlantic(vector<vector<int>>& matrix) {
        vector<vector<int>> &a = matrix;
        int n = matrix.size();
        int m = n > 0 ? matrix[0].size() : 0;
        vector<pair<int, int>> res;
        if (n == 0 || m == 0) {
            return res;
        }
        
        int i, j;
        vector<vector<bool>> pa(n, vector<bool>(m, false));
        for (i = 0; i <= m - 1; ++i) {
            pa[0][i] = true;
        }
        for (i = 0; i <= n - 1; ++i) {
            pa[i][0] = true;
        }
        for (i = 1; i <= m - 1; ++i) {
            flood(0, i, n, m, matrix, pa);
        }
        for (i = 1; i <= n - 1; ++i) {
            flood(i, 0, n, m, matrix, pa);
        }
        
        vector<vector<bool>> at(n, vector<bool>(m, false));
        for (i = m - 1; i >= 0; --i) {
            at[n - 1][i] = true;
        }
        for (i = n - 1; i >= 0; --i) {
            at[i][m - 1] = true;
        }
        for (i = m - 2; i >= 0; --i) {
            flood(n - 1, i, n, m, matrix, at);
        }
        for (i = n - 2; i >= 0; --i) {
            flood(i, m - 1, n, m, matrix, at);
        }
        
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (pa[i][j] && at[i][j]) {
                    res.push_back(make_pair(i, j));
                }
            }
        }
        pa.clear();
        at.clear();
        return res;
    }
private:
    void flood(int x, int y, int n, int m, vector<vector<int>> &matrix, 
               vector<vector<bool>> &b) {
        int i;
        int x1, y1;
        for (i = 0; i < 4; ++i) {
            x1 = x + dir[i][0];
            y1 = y + dir[i][1];
            if (x1 < 0 || x1 > n - 1 || y1 < 0 || y1 > m - 1) {
                continue;
            }
            if (b[x1][y1]) {
                continue;
            }
            if (matrix[x1][y1] < matrix[x][y]) {
                continue;
            }
            b[x1][y1] = true;
            flood(x1, y1, n, m, matrix, b);
        }
    }
};
