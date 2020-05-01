// Save your bits
class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int n = board.size();
        int m = n > 0 ? board[0].size() : 0;
        if (n == 0 || m == 0) {
            return;
        }
        int i, j, k;
        static const int d[8][2] = {
            {-1, -1}, {-1, +1}, {+1, -1}, {+1, +1}, 
            {-1, 0}, {+1, 0}, {0, -1}, {0, +1}
        };
        
        int cnt;
        int i1, j1;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                cnt = 0;
                for (k = 0; k < 8; ++k) {
                    i1 = i + d[k][0];
                    if (i1 < 0 || i1 > n - 1) {
                        continue;
                    }
                    j1 = j + d[k][1];
                    if (j1 < 0 || j1 > m - 1) {
                        continue;
                    }
                    if (board[i1][j1] & 1) {
                        ++cnt;
                    }
                }
                if (board[i][j] & 1) {
                    if (cnt >= 2 && cnt <= 3) {
                        board[i][j] |= 2;
                    }
                } else {
                    if (cnt == 3) {
                        board[i][j] |= 2;
                    }
                }
            }
        }
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                board[i][j] >>= 1;
            }
        }
    }
};
