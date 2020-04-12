class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size();
        int m = n > 0 ?  grid[0].size() : 0;
        if (n == 0 || m == 0) {
            return 0;
        }
        
        int i, j;
        int res = 0;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (grid[i][j] == '0') {
                    continue;
                }
                ++res;
                dfs(i, j, grid, n, m);
            }
        }
        return res;
    }
private:
    void dfs(int i, int j, vector<vector<char>> &grid, int n, int m) {
        static const int dir[4][2] = {{-1, 0}, {+1, 0}, {0, -1}, {0, +1}};
        
        grid[i][j] = '0';
        int k;
        int i1, j1;
        for (k = 0; k < 4; ++k) {
            i1 = i + dir[k][0];
            j1 = j + dir[k][1];
            if (i1 < 0 || i1 > n - 1 || j1 < 0 || j1 > m - 1) {
                continue;
            }
            if (grid[i1][j1] == '0') {
                continue;
            }
            dfs(i1, j1, grid, n, m);
        }
    }
};
