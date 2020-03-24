// O(1) space, one pass, no modification.
// Just think twice before you start coding.
// 子曰：“再斯可矣。”
class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        n = board.size();
        m = n > 0 ? board[0].size() : 0;
        if (n == 0 || m == 0) {
            return 0;
        }
        int i, j;
        int cnt = 0;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (board[i][j] == '.') {
                    continue;
                }
                if (inbound(i - 1, j) && board[i - 1][j] != '.') {
                    continue;
                }
                if (inbound(i, j - 1) && board[i][j - 1] != '.') {
                    continue;
                }
                ++cnt;
            }
        }
        return cnt;
    }
private:
    int n;
    int m;
    
    bool inbound(int x, int y) {
        return x >= 0 && x <= n - 1 && y >= 0 && y <= m - 1;
    }
};
