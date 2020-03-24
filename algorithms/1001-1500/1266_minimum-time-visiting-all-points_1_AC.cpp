// https://leetcode.com/problems/minimum-time-visiting-all-points/
#include <algorithm>
#include <cmath>
#include <vector>
using std::abs;
using std::max;
using std::vector;

class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        vector<vector<int>> &a = points;
        int n = a.size();
        int i;
        int res = 0;
        for (i = 0; i + 1 < n; ++i) {
            res += max(abs(a[i][0] - a[i + 1][0]), abs(a[i][1] - a[i + 1][1]));
        }
        return res;
    }
};
