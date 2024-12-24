// easy
// https://leetcode.com/problems/largest-number-at-least-twice-of-others/
#include <algorithm>
using std::max;

class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int n = nums.size();
        int mi = 0;
        int i;
        for (i = 1; i < n; ++i) {
            if (nums[i] >= nums[mi]) {
                mi = i;
            }
        }
        for (i = 0; i < n; ++i) {
            if (i == mi) {
                continue;
            }
            if (nums[i] * 2 > nums[mi]) {
                return -1;
            }
        }
        return mi;
    }
};
