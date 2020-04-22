class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int m = n > 0 ? matrix[0].size() : 0;
        if (n == 0 || m == 0) {
            return;
        }
        bool r0 = false;
        bool c0 = false;
        int i, j;
        for (i = 0; i < n; ++i) {
            if (matrix[i][0] == 0) {
                c0 = true;
            }
        }
        for (j = 0; j < m; ++j) {
            if (matrix[0][j] == 0) {
                r0 = true;
            }
        }
        for (i = 1; i < n; ++i) {
            for (j = 1; j < m; ++j) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = matrix[0][j] = 0;
                }
            }
        }
        for (i = 1; i < n; ++i) {
            if (matrix[i][0] != 0) {
                continue;
            }
            for (j = 0; j < m; ++j) {
                matrix[i][j] = 0;
            }
        }
        for (j = 1; j < m; ++j) {
            if (matrix[0][j] != 0) {
                continue;
            }
            for (i = 0; i < n; ++i) {
                matrix[i][j] = 0;
            }
        }
        if (r0) {
            for (j = 0; j < m; ++j) {
                matrix[0][j] = 0;
            }
        }
        if (c0) {
            for (i = 0; i < n; ++i) {
                matrix[i][0] = 0;
            }
        }
    }
};