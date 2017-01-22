#include <algorithm>
using std::max;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) {
            return true;
        }
        int idx = 0;
        int i;
        for (i = 0; i < n; ++i) {
            if (idx < i) {
                return false;
            }
            idx = max(idx, i + nums[i]);
        }
        return true;
    }
};
