#include <vector>
using std::vector;

static const int NUM_DIR = 8;
static const int offset[NUM_DIR][2] = {
    {-1, 0}, {+1, 0}, {0, -1}, {0, +1}, 
    {-1, -1}, {-1, +1}, {+1, -1}, {+1, +1}
};

class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        auto &b = board;
        int n = b.size();
        int m = (n > 0 ? b[0].size() : 0);
        if (n == 0 || m == 0) {
            return b;
        }
        
        int x = click[0];
        int y = click[1];
        reveal(x, y, b, n, m);
        
        return b;
    }
private:
    void reveal(int x, int y, vector<vector<char>> &b, int n, int m) {
        if (x < 0 || x > n - 1 || y < 0 || y > m - 1) {
            return;
        }
        if (b[x][y] != 'E' && b[x][y] != 'M') {
            return;
        }
        if (b[x][y] == 'M') {
            b[x][y] = 'X';
            return;
        }
        
        int i;
        int x1, y1;
        int mc = 0;
        for (i = 0; i < NUM_DIR; ++i) {
            x1 = x + offset[i][0];
            y1 = y + offset[i][1];
            if (x1 < 0 || x1 > n - 1 || y1 < 0 || y1 > m - 1) {
                continue;
            }
            if (b[x1][y1] == 'M') {
                ++mc;
            }
        }
        
        if (mc > 0) {
            b[x][y] = mc + '0';
            return;
        }
        b[x][y] = 'B';
        for (i = 0; i < 8; ++i) {
            x1 = x + offset[i][0];
            y1 = y + offset[i][1];
            if (x1 < 0 || x1 > n - 1 || y1 < 0 || y1 > m - 1) {
                continue;
            }
            if (b[x1][y1] == 'E') {
                reveal(x1, y1, b, n, m);
            }
        }
    }
};
