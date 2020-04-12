class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        static const int dir[] = {1, 2, 3, 0};
        static const int offset[][2] = {{0, +1}, {+1, 0}, {0, -1}, {-1, 0}};
        
        vector<int> res;
        int n = matrix.size();
        int m = n > 0 ? matrix[0].size() : 0;
        if (n == 0 || m == 0) {
            return res;
        }
        
        vector<vector<bool>> mark(n, vector<bool>(m, false));
        int i, j, k;
        int i1, j1;
        int d;
        int cnt;
        
        cnt = n * m;
        i = j = 0;
        d = 0;
        while (true) {
            res.push_back(matrix[i][j]);
            mark[i][j] = true;
            if (--cnt == 0) {
                break;
            }
            for (k = 0; k < 4; ++k) {
                i1 = i + offset[d][0];
                j1 = j + offset[d][1];
                if (i1 >= 0 && i1 <= n - 1 && j1 >= 0 && j1 <= m - 1 && 
                    !mark[i1][j1]) {
                    i = i1;
                    j = j1;
                    break;
                }
                d = dir[d];
            }
        }
        mark.clear();
        return res;
    }
};
