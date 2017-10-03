class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& M) {
        int n = M.size();
        int m = M[0].size();
        vector<vector<int>> M1(n, vector<int>(m, 0));
        
        static int offset[9][2] = {
            {-1, -1}, {-1,  0}, {-1, +1}, 
            { 0, -1}, { 0,  0}, { 0, +1}, 
            {+1, -1}, {+1,  0}, {+1, +1}
        };
        
        int i, j;
        int i1, j1;
        int k;
        int cc;
        int sum;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                sum = 0;
                cc = 0;
                for (k = 0; k < 9; ++k) {
                   i1 = i + offset[k][0];
                   j1 = j + offset[k][1];
                   if (i1 < 0 || i1 > n - 1 || j1 < 0 || j1 > m - 1) {
                       continue;
                   }
                   sum += M[i1][j1];
                   ++cc;
                }
                M1[i][j] = sum / cc;
            }
        }
        
        return M1;
    }
};
