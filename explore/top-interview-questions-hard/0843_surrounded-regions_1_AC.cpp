// No need to use flooding.
#include <unordered_set>
using std::unordered_set;

class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int n = board.size();
        int m = n > 0 ? board[0].size() : 0;
        if (n == 0 || m == 0) {
            return;
        }
        vector<int> dj(n * m);
        int nm = dj.size();
        int i, j;
        for (i = 0; i < nm; ++i) {
            dj[i] = i;
        }
        
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (board[i][j] != 'O') {
                    continue;
                }
                if (i > 0 && board[i - 1][j] == 'O') {
                    dj[findRoot(dj, i * m + j)] = findRoot(dj, (i - 1) * m + j);
                }
                if (j > 0 && board[i][j - 1] == 'O') {
                    dj[findRoot(dj, i * m + j)] = findRoot(dj, i * m + (j - 1));
                }
            }
        }
        
        unordered_set<int> us;
        for (i = 0; i < n; ++i) {
            if (board[i][0] == 'O') {
                us.insert(findRoot(dj, i * m));
            }
            if (board[i][m - 1] == 'O') {
                us.insert(findRoot(dj, i * m + (m - 1)));
            }
        }
        for (j = 0; j < m; ++j) {
            if (board[0][j] == 'O') {
                us.insert(findRoot(dj, j));
            }
            if (board[n - 1][j] == 'O') {
                us.insert(findRoot(dj, (n - 1) * m + j));
            }
        }
        
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (board[i][j] != 'O' || 
                    us.find(findRoot(dj, i * m + j)) != us.end()) {
                    continue;
                }
                board[i][j] = 'X';
            }
        }
        dj.clear();
        us.clear();
    }
private:
    int findRoot(vector<int> &dj, int x) {
        int r = x;
        while (r != dj[r]) {
            r = dj[r];
        }
        int k = x;
        while (k != r) {
            x = dj[x];
            dj[k] = r;
            k = x;
        }
        return r;
    }
};
