#include <algorithm>
using std::max;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) {
            return 0;
        }
        int res = nums[0];
        int i;
        for (i = 1; i < n; ++i) {
            res = max(res, nums[i]);
        }
        if (res <= 0) {
            return res;
        }
        int sum = 0;
        res = 0;
        for (i = 0; i < n; ++i) {
            sum += nums[i];
            sum = max(sum, 0);
            res = max(res, sum);
        }
        return res;
    }
};
