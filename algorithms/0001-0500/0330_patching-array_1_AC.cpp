// The key is to figure out why it is greedy.
#include <algorithm>
#include <cstdint>
using std::max;

class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        int na = nums.size();
        int res = 0;
        int64_t max_val = 0;
        
        int i = 0;
        while (max_val < n) {
            if (i < na && nums[i] <= max_val + 1) {
                max_val += nums[i];
                ++i;
            } else {
                max_val += max_val + 1;
                ++res;
            }
        }
        
        return res;
    }
};
