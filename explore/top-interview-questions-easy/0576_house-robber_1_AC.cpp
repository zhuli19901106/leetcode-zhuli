#include <algorithm>
using std::max;

class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        int f1, f2, f3;
        f1 = f2 = f3 = 0;
        int  i;
        for (i = 0; i < n; ++i) {
            f3 = max(f1 + nums[i], f2);
            f1 = f2;
            f2 = f3;
        }
        return f3;
    }
};
