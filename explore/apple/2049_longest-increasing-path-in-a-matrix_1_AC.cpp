// Sort everything before DP.
#include <algorithm>
#include <vector>
using std::max;
using std::sort;
using std::vector;

static const int offset[4][2] = {{-1, 0}, {+1, 0}, {0, -1}, {0, +1}};

typedef struct Grid {
    int x;
    int y;
    int h;
    
    Grid(int _x = 0, int _y = 0, int _h = 0): x(_x), y(_y), h(_h) {}
} Grid;

bool comparator(const Grid &g1, const Grid &g2)
{
    return g1.h > g2.h;
}

class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        auto &a = matrix;
        int n = a.size();
        int m = n > 0 ? a[0].size() : 0;
        if (n == 0 || m == 0) {
            return 0;
        }
        
        vector<Grid> v;
        int i, j;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                v.push_back(Grid(i, j, a[i][j]));
            }
        }
        sort(v.begin(), v.end(), comparator);
        
        vector<vector<int>> dp(n, vector<int>(m, 1));
        int nm = n * m;
        Grid g, g1;
        for (i = 0; i < nm; ++i) {
            g = v[i];
            for (j = 0; j < 4; ++j) {
                g1.x = g.x + offset[j][0];
                g1.y = g.y + offset[j][1];
                if (g1.x < 0 || g1.x > n - 1 || g1.y < 0 || g1.y > m - 1) {
                    continue;
                }
                if (a[g1.x][g1.y] <= a[g.x][g.y]) {
                    continue;
                }
                dp[g.x][g.y] = max(dp[g.x][g.y], dp[g1.x][g1.y] + 1);
            }
        }
        v.clear();
        
        int res = 0;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                res = max(res, dp[i][j]);
            }
        }
        dp.clear();
        
        return res;
    }
};
