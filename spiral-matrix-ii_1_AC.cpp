enum {
    LEFT = 0, DOWN, RIGHT, UP
};

static int next_dirs[4] = {UP, LEFT, DOWN, RIGHT};
static int offset[4][2] = {{0, -1}, {+1, 0}, {0, +1}, {-1, 0}};

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> res(n, vector<int>(n, 0));
        if (n == 0) {
            return res;
        }
        
        int x = 0, y = 0;
        int x1, y1;
        int dir = RIGHT;
        int cnt = 0;
        int i;
        while (true) {
            res[x][y] = ++cnt;
            if (cnt == n * n) {
                break;
            }
            for (i = 0; i < 4; ++i) {
                x1 = x + offset[dir][0];
                y1 = y + offset[dir][1];
                if ((x1 >= 0 && x1 <= n - 1) && (y1 >= 0 && y1 <= n - 1)
                    && res[x1][y1] == 0) {
                    x = x1;
                    y = y1;
                    break;
                } else {
                    dir = next_dirs[dir];
                }
            }
        }
        return res;
    }
};
