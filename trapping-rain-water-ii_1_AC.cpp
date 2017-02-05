#include <algorithm>
#include <funtional>
#include <queue>
#include <vector>
using std::greater;
using std::max;
using std::priority_queue;
using std::vector;

static const int offset[4][2] = {{-1, 0}, {+1, 0}, {0, -1}, {0, +1}};

typedef struct Grid {
    int x;
    int y;
    int h;
    
    Grid(int _x = 0, int _y = 0, int _h = 0): x(_x), y(_y), h(_h) {}
    
    bool operator < (const Grid &g) const {
        return h < g.h;
    }
    
    bool operator > (const Grid &g) const {
        return h > g.h;
    }
} Grid;

class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        auto &a = heightMap;
        int n = a.size();
        int m = n > 0 ? a[0].size() : 0;
        if (n == 0 || m == 0) {
            return 0;
        }
        
        vector<vector<bool>> v(n, vector<bool>(m, false));
        int i, j, k;
        priority_queue<Grid, vector<Grid>, greater<Grid>> pq;
        
        for (i = 0; i <= n - 1; ++i) {
            pq.push(Grid(i, 0, a[i][0]));
            v[i][0] = true;
            pq.push(Grid(i, m - 1, a[i][m - 1]));
            v[i][m - 1] = true;
        }
        for (j = 0; j <= m - 1; ++j) {
            pq.push(Grid(0, j, a[0][j]));
            v[0][j] = true;
            pq.push(Grid(n - 1, j, a[n - 1][j]));
            v[n  -1][j] = true;
        }
        
        Grid g, g1;
        int res = 0;
        while (!pq.empty()) {
            g = pq.top();
            pq.pop();
            for (k = 0; k < 4; ++k) {
                g1.x = g.x + offset[k][0];
                g1.y = g.y + offset[k][1];
                if (g1.x < 0 || g1.x > n - 1 || g1.y < 0 || g1.y > m - 1) {
                    continue;
                }
                if (v[g1.x][g1.y]) {
                    continue;
                }
                res += max(0, g.h - a[g1.x][g1.y]);
                g1.h = max(g.h, a[g1.x][g1.y]);
                pq.push(g1);
                v[g1.x][g1.y] = true;
            }
        }
        
        v.clear();
        return res;
    }
};
