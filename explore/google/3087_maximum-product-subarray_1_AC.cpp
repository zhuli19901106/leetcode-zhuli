// O(n) time and O(1) space.
#include <algorithm>
using std::max;
using std::min;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) {
            return nums[0];
        }
        int i;
        int last_min, cur_min;
        int last_max, cur_max;
        int res;
        
        res = last_min = last_max = nums[0];
        for (i = 1; i < n; ++i) {
            cur_min = min(nums[i], min(nums[i] * last_min, nums[i] * last_max));
            cur_max = max(nums[i], max(nums[i] * last_min, nums[i] * last_max));
            res = max(res, cur_max);
            last_min = cur_min;
            last_max = cur_max;
        }
        return res;
    }
};
