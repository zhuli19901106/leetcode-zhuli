#include <algorithm>
using std::min;

class Solution {
public:
    int minMoves(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) {
            return 0;
        }
        int min_val = nums[0];
        int i;
        for (i = 1; i < n; ++i) {
            min_val = min(min_val, nums[i]);
        }
        int res = 0;
        for (i = 0; i < n; ++i) {
            res += nums[i] - min_val;
        }
        return res;
    }
};
