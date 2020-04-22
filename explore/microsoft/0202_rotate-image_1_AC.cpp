class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        vector<vector<int>> &a = matrix;
        int n = a.size();
        if (n < 2) {
            return;
        }
        int i, j;
        int tmp;
        for (i = 0; i < (n + 1) / 2; ++i) {
            for (j = 0; j < n / 2; ++j) {
                tmp = a[i][j];
                a[i][j] = a[n - 1 - j][i];
                a[n - 1 - j][i] = a[n - 1 - i][n - 1 - j];
                a[n - 1 - i][n - 1 - j] = a[j][n - 1 - i];
                a[j][n - 1 - i] = tmp;
            }
        }
    }
};
