class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int i, j;
        for (i = 0; i < N2; ++i) {
            for (j = 0; j < N2; ++j) {
                row[i][j] = col[i][j] = block[i][j] = false;
            }
        }
        
        int d;
        for (i = 0; i < N2; ++i) {
            for (j = 0; j < N2; ++j) {
                if (board[i][j] == '.') {
                    continue;
                }
                
                d = board[i][j] - '1';
                if (row[i][d]) {
                    return false;
                }
                row[i][d] = true;
                if (col[j][d]) {
                    return false;
                }
                col[j][d] = true;
                if (block[i / N * N + j / N][d]) {
                    return false;
                }
                block[i / N * N + j / N][d] = true;
            }
        }
        return true;
    }
private:
    static const int N = 3;
    static const int N2 = N * N;
    bool row[N2][N2];
    bool col[N2][N2];
    bool block[N2][N2];
};
