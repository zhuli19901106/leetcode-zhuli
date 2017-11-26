#include <queue>
#include <vector>
using std::queue;
using std::vector;

class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        int n = image.size();
        int m = n > 0 ? image[0].size() : 0;
        if (n == 0 || m == 0) {
            return image;
        }
        
        if (image[sr][sc] == newColor) {
            return image;
        }
        
        int oldColor = image[sr][sc];
        int i, i1;
        int x, y;
        int x1, y1;
        static int offset[4][2] = {{-1, 0}, {+1, 0}, {0, -1}, {0, +1}};
        int k;
        
        queue<int> q;
        q.push(sr * m + sc);
        while (!q.empty()) {
            i = q.front();
            q.pop();
            x = i / m;
            y = i % m;
            image[x][y] = newColor;
            for (k = 0; k < 4; ++k) {
                x1 = x + offset[k][0];
                y1 = y + offset[k][1];
                if (inbound(x1, y1, n, m) && image[x1][y1] == oldColor) {
                    q.push(x1 * m + y1);
                }
            }
        }
        return image;
    }
private:
    bool inbound(int x, int y, int n, int m) {
        return x >= 0 && x <= n - 1 && y >= 0 && y <= m - 1;
    }
};
