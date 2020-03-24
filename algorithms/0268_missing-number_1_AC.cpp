#include <cstdint>

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int64_t sum = 0;
        int n = nums.size();
        int i;
        for (i = 0; i < n; ++i) {
            sum += nums[i];
        }
        return 1LL * n * (n + 1) / 2 - sum;
    }
};
