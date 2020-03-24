class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int n = board.size();
        int m = n > 0 ? board[0].size() : 0;
        if (word.size() == 0) {
            return true;
        }
        if (n == 0 || m == 0) {
            return false;
        }
        vector<vector<bool>> mark(n, vector<bool>(m, false));
        int i, j;
        bool res;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (board[i][j] != word[0]) {
                    continue;
                }
                mark[i][j] = true;
                res = dfs(1, i, j, word, board, mark, n, m);
                mark[i][j] = false;
                if (res) {
                    return true;
                }
            }
        }
        mark.clear();
        return false;
    }
private:
    bool dfs(int idx, int x, int y, string &s, vector<vector<char>> &board, 
        vector<vector<bool>> &mark, int n, int m) {
        if (idx == s.size()) {
            return true;
        }
        
        static const int dir[4][2] = {{-1, 0}, {+1, 0}, {0, -1}, {0, +1}};
        int x1, y1;
        int i;
        bool res;
        for (i = 0; i < 4; ++i) {
            x1 = x + dir[i][0];
            y1 = y + dir[i][1];
            if (x1 < 0 || x1 > n - 1 || y1 < 0 || y1 > m - 1 || mark[x1][y1]) {
                continue;
            }
            if (board[x1][y1] != s[idx]) {
                continue;
            }
            mark[x1][y1] = true;
            res = dfs(idx + 1, x1, y1, s, board, mark, n, m);
            mark[x1][y1] = false;
            if (res) {
                return true;
            }
        }
        return false;
    }
};
