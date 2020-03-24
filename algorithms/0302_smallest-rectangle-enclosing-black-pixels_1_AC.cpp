// This problem is boring.
// Why is it rated "hard"?
#include <algorithm>
#include <vector>
using std::max;
using std::min;
using std::vector;

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
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (a[i][j] != '1') {
                    continue;
                }
                min_x = min(min_x, i);
                max_x = max(max_x, i);
                min_y = min(min_y, j);
                max_y = max(max_y, j);
            }
        }
        return (max_x - min_x + 1) * (max_y - min_y + 1);
    }
};
