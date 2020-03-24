#include <vector>
using std::vector;

class TicTacToe {
public:
    /** Initialize your data structure here. */
    TicTacToe(int n) {
        winner = 0;
        this->n = n;
        b.resize(n, vector<int>(n, 0));
    }
    
    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    int move(int row, int col, int player) {
        static const int offset[4][2] = {{-1, 0}, {0, -1}, {-1, -1}, {-1, +1}};
        
        if (winner != 0) {
            return winner;
        }
        
        if (!inbound(row, col)) {
            return 0;
        }
        if (b[row][col] != 0) {
            return winner;
        }
        
        b[row][col] = player;
        int k;
        int i, j;
        int cnt;
        for (k = 0; k < 4; ++k) {
            cnt = -1;
            i = row;
            j = col;
            while (inbound(i, j) && b[i][j] == player) {
                ++cnt;
                i += offset[k][0];
                j += offset[k][1];
            }
            
            i = row;
            j = col;
            while (inbound(i, j) && b[i][j] == player) {
                ++cnt;
                i -= offset[k][0];
                j -= offset[k][1];
            }
            if (cnt >= n) {
                return winner = player;
            }
        }
        return winner;
    }
private:
    int winner;
    
    vector<vector<int>> b;
    int n;
    
    bool inbound(int x, int y) {
        return x >= 0 && x <= n - 1 && y >= 0 && y <= n - 1;
    }
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe obj = new TicTacToe(n);
 * int param_1 = obj.move(row,col,player);
 */
