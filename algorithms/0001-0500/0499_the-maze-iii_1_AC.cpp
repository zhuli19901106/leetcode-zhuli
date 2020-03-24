// Sometimes it's easy to figure out a solution, but hard to write it down clean and short.
// I hate the word "lexicographically".
#include <algorithm>
#include <climits>
#include <queue>
#include <string>
#include <vector>
using std::priority_queue;
using std::reverse;
using std::string;
using std::vector;

static const int offset[4][2] = {{+1, 0}, {0, -1}, {0, +1}, {-1, 0}};
static const string sd = "dlru";

struct Grid;
typedef struct Grid Grid;
struct Grid {
    int x, y;
    int d;
    string p;
    
    Grid(int _x = 0, int _y = 0, int _d = 0, string _p = ""): 
        x(_x), y(_y), d(_d), p(_p) {}
    
    bool operator < (const Grid &g) const {
        if (d != g.d) {
            return d > g.d;
        }
        return p > g.p;
    }
};

class Solution {
public:
    string findShortestWay(vector<vector<int>>& maze, vector<int>& ball, vector<int>& hole) {
        auto &a = maze;
        n = a.size();
        m = a[0].size();
        
        int sx = ball[0];
        int sy = ball[1];
        int ex = hole[0];
        int ey = hole[1];
        
        vector<vector<Grid>> v(n, vector<Grid>(m));
        int x, y;
        for (x = 0; x < n; ++x) {
            for (y = 0; y < m; ++y) {
                v[x][y].x = x;
                v[x][y].y = y;
                v[x][y].d = INT_MAX;
            }
        }
        
        priority_queue<Grid> pq;
        int i;
        int d1;
        int x1, y1;
        int x2, y2;
        Grid g;
        
        pq.push(Grid(sx, sy, 0, ""));
        while (!pq.empty() && v[ex][ey].d == INT_MAX) {
            g = pq.top();
            x = g.x;
            y = g.y;
            pq.pop();
            if (v[x][y].d != INT_MAX) {
                continue;
            } else {
                v[x][y] = g;
            }
            
            for (i = 0; i < 4; ++i) {
                x1 = x;
                y1 = y;
                d1 = 0;
                while (true) {
                    x2 = x1 + offset[i][0];
                    y2 = y1 + offset[i][1];
                    if (inbound(x2, y2) && a[x2][y2] == 0) {
                        x1 = x2;
                        y1 = y2;
                        ++d1;
                        if (x1 == ex && y1 == ey) {
                            break;
                        }
                    } else {
                        break;
                    }
                }
                if (d1 > 0 && v[x1][y1].d == INT_MAX) {
                    pq.push(Grid(x1, y1, g.d + d1, g.p + sd[i]));
                }
            }
        }
        while (!pq.empty()) {
            pq.pop();
        }
        
        string res = (v[ex][ey].d == INT_MAX ? "impossible" : v[ex][ey].p);
        v.clear();
        
        return res;      
    }
private:
    int n, m;
    
    bool inbound(int x, int y) {
        return x >= 0 && x <= n - 1 && y >= 0 && y <= m - 1;
    }
};
