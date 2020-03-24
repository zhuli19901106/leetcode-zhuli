#include <algoithm>
using std::min;

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        if (n == 0) {
            return 0;
        }
        int i, j;
        for (i = 1; i < n; ++i) {
            triangle[i][0] += triangle[i - 1][0];
            for (j = 1; j < i; ++j) {
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j]);
            }
            triangle[i][i] += triangle[i - 1][i - 1];
        }
        int res = triangle[n - 1][0];
        for (i = 1; i < n; ++i) {
            res = min(res, triangle[n - 1][i]);
        }
        return res;
    }
};
