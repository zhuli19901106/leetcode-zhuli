#include <queue>
#include <vector>
using std::queue;
using std::vector;

static const int INF = 2147483647;
static const int offset[4][2] = {{-1, 0}, {+1, 0}, {0, -1}, {0, +1}};

typedef struct Pos {
    int x, y;
    int d;
    
    Pos(int _x = 0, int _y = 0, int _d = 0): x(_x), y(_y), d(_d) {}
} Pos;

class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        auto &a = rooms;
        int n = a.size();
        int m = (n > 0 ? a[0].size() : 0);
        if (n == 0 || m == 0) {
            return;
        }
        
        queue<Pos> q;
        Pos p;
        int i, j;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (a[i][j] != 0) {
                    continue;
                }
                q.push(Pos(i, j, 0));
            }
        }
        
        int k;
        while (!q.empty()) {
            p = q.front();
            q.pop();
            
            for (k = 0; k < 4; ++k) {
                i = p.x + offset[k][0];
                j = p.y + offset[k][1];
                if (i < 0 || i > n - 1 || j < 0 || j > m - 1) {
                    continue;
                }
                if (a[i][j] != INF) {
                    continue;
                }
                a[i][j] = p.d + 1;
                q.push(Pos(i, j, a[i][j]));
            }
        }
    }
};
