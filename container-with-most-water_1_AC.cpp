#include <algorithm>
using std::max;
using std::min;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int res = 0;
        int n = height.size();
        int i = 0;
        int j = n - 1;
        while (i < j) {
            res = max(res, min(height[i], height[j]) * (j - i));
            if (height[i] < height[j]) {
                ++i;
            } else {
                --j;
            }
        }
        return res;
    }
};
