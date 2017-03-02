#include <vector>
using std::vector;

static const int offset[4][2] = {{-1, 0}, {+1, 0}, {0, -1}, {0, +1}};

class Solution {
public:
    bool hasPath(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        auto &a = maze;
        n = a.size();
        m = a[0].size();
        
        sx = start[0];
        sy = start[1];
        ex = destination[0];
        ey = destination[1];
        
        b.resize(n, vector<bool>(m, false));
        b[sx][sy] = true;
        dfs(sx, sy, a);
        
        bool res = b[ex][ey];
        b.clear();
        
        return res;
    }
private:
    int n, m;
    int sx, sy;
    int ex, ey;
    vector<vector<bool>> b;
    
    bool inbound(int x, int y) {
        return x >= 0 && x <= n - 1 && y >= 0 && y <= m - 1;
    }
    
    void dfs(int x, int y, vector<vector<int>> &a) {
        if (b[ex][ey]) {
            return;
        }
        
        int i;
        int x1, y1;
        int x2, y2;
        for (i = 0; i < 4; ++i) {
            x1 = x;
            y1 = y;
            while (true) {
                x2 = x1 + offset[i][0];
                y2 = y1 + offset[i][1];
                if (inbound(x2, y2) && a[x2][y2] == 0) {
                    x1 = x2;
                    y1 = y2;
                } else {
                    break;
                }
            }
            if (b[x1][y1]) {
                continue;
            }
            b[x1][y1] = true;
            dfs(x1, y1, a);
        }
    }
};
