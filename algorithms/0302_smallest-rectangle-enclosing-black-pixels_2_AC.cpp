// Flood fill with BFS
#include <algorithm>
#include <queue>
#include <utility>
#include <vector>
using std::max;
using std::make_pair;
using std::min;
using std::pair;
using std::queue;
using std::vector;

static const int offset[4][2] = {{-1, 0}, {+1, 0}, {0, -1}, {0, +1}};

class Solution {
public:
    int minArea(vector<vector<char>>& image, int x, int y) {
        auto &a = image;
        int n = a.size();
        int m = a[0].size();
        int min_x, min_y, max_x, max_y;
        min_x = max_x = x;
        min_y = max_y = y;
        
        int i, j;
        int i1, j1;
        int k;
        queue<pair<int, int>> q;
        
        a[x][y] = '0';
        q.push(make_pair(x, y));
        while (!q.empty()) {
            i = q.front().first;
            j = q.front().second;
            min_x = min(min_x, i);
            max_x = max(max_x, i);
            min_y = min(min_y, j);
            max_y = max(max_y, j);
            q.pop();
            
            for (k = 0; k < 4; ++k) {
                i1 = i + offset[k][0];
                j1 = j + offset[k][1];
                if (i1 < 0 || i1 > n - 1 || j1 < 0 || j1 > m - 1) {
                    continue;
                }
                if (a[i1][j1] != '1') {
                    continue;
                }
                a[i1][j1] = '0';
                q.push(make_pair(i1, j1));
            }
        }
        
        return (max_x - min_x + 1) * (max_y - min_y + 1);
    }
};
