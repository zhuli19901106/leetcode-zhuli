// Each op is O(1) after preprocessing.
class NumMatrix {
public:
    NumMatrix(vector<vector<int>> matrix) {
        n = matrix.size();
        m = n > 0 ? matrix[0].size() : 0;
        s.resize(n + 1, vector<int>(m + 1, 0));
        
        int i, j;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + 
                    matrix[i][j];
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        return s[row2 + 1][col2 + 1] + s[row1][col1] - s[row2 + 1][col1] - 
            s[row1][col2 + 1];
    }
    
    ~NumMatrix() {
        s.clear();
    }
private:
    vector<vector<int>> s;
    int n;
    int m;
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */
