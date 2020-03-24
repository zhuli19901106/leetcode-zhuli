#include <algorithm>
using std::min;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = n > 0 ? grid[0].size() : 0;
        if (n == 0 || m == 0) {
            return 0;
        }
        int i, j;
        for (i = 1; i < n; ++i) {
            grid[i][0] += grid[i - 1][0];
        }
        for (i = 1; i < m; ++i) {
            grid[0][i] += grid[0][i - 1];
        }
        for (i = 1; i < n; ++i) {
            for (j = 1; j < m; ++j) {
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1]);
            }
        }
        return grid[n - 1][m - 1];
    }
};
