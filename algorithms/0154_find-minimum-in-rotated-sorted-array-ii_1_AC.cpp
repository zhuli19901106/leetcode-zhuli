#include <algorithm>
using std::min;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) {
            return nums[0];
        }
        
        int ll, rr, mm;
        ll = 0;
        rr = n - 1;
        while (rr - ll > 1) {
            if (nums[ll] == nums[rr]) {
                --rr;
                continue;
            }
            if (nums[ll] < nums[rr]) {
                break;
            }
            mm = ll + (rr - ll >> 1);
            if (nums[mm] > nums[rr]) {
                ll = mm;
            } else {
                rr = mm;
            }
        }
        return min(nums[ll], nums[rr]);
    }
};
