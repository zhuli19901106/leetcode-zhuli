class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        n = grid.size();
        m = n ? grid[0].size() : 0;
        int res = 0;
        int i, j, k;
        int i1, j1;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (grid[i][j] == 0) {
                    continue;
                }
                res += 4;
                for (k = 0; k < 4; ++k) {
                    i1 = i + dir[k][0];
                    j1 = j + dir[k][1];
                    if (inbound(i1, j1) && grid[i1][j1] != 0) {
                        --res;
                    }
                }
            }
        }
        return res;
    }
private:
    int n;
    int m;
    int dir[4][2] = {{-1, 0}, {+1, 0}, {0, -1}, {0, +1}};
    
    bool inbound(int x, int y) {
        return (x >= 0 && x <= n - 1) && (y >= 0 && y <= m - 1);
    }
};
