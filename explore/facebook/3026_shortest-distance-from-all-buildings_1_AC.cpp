// If you have to search something, pick your target and direction carefully.
#include <climits>
#include <queue>
#include <unordered_map>
#include <vector>
using std::unordered_map;
using std::vector;

static const int offset[4][2] = {{-1, 0}, {+1, 0}, {0, -1}, {0, +1}};

class Solution {
public:
    int shortestDistance(vector<vector<int>>& grid) {
        auto &g = grid;
        int n = g.size();
        int m = (n > 0 ? g[0].size() : 0);
        if (n == 0 || m == 0) {
            return -1;
        }
        
        unordered_map<int, int> um;
        int i, j;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (g[i][j] == 0) {
                    um[i * m + j] = 0;
                }
            }
        }
        
        int x, y;
        int x1, y1;
        int val;
        queue<int> q;
        vector<vector<int>> d(n, vector<int>(m));
        int k;
        
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (g[i][j] != 1) {
                    continue;
                }
                for (x = 0; x < n; ++x) {
                    for (y = 0; y < m; ++y) {
                        d[x][y] = INT_MAX;
                    }
                }
                
                // Begin the search from a building.
                d[i][j] = 0;
                q.push(i * m + j);
                while (!q.empty()) {
                    val = q.front();
                    q.pop();
                    
                    x = val / m;
                    y = val % m;
                    for (k = 0; k < 4; ++k) {
                        x1 = x + offset[k][0];
                        y1 = y + offset[k][1];
                        if (x1 < 0 || x1 > n - 1 || y1 < 0 || y1 > m - 1) {
                            continue;
                        }
                        if (g[x1][y1] != 0 || d[x1][y1] != INT_MAX) {
                            continue;
                        }
                        d[x1][y1] = d[x][y] + 1;
                        q.push(x1 * m + y1);
                        
                        um[x1 * m + y1] += d[x1][y1];
                    }
                }
                
                // If we can't reach a '0' from a '1', vice versa.
                // So we mark this '0' as '2'.
                auto it = um.begin();
                while (it != um.end()) {
                    x = it->first / m;
                    y = it->first % m;
                    if (d[x][y] == INT_MAX) {
                        g[x][y] = 2;
                        it = um.erase(it);
                    } else {
                        ++it;
                    }
                }
            }
        }
        if (um.size() == 0) {
            return -1;
        }
        
        int res = INT_MAX;
        for (auto &p: um) {
            res = min(res, p.second);
        }
        um.clear();
        
        return res;
    }
};
