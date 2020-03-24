// Messy.
#include <climits>

class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int n = nums.size();
        int cc = 0;
        int maxval = INT_MIN, old_maxval = INT_MIN;
        
        int i;
        for (i = 0; i < n; ++i) {
            if (nums[i] >= maxval) {
                old_maxval = maxval;
                maxval = nums[i];
            } else {
                if (cc > 0) {
                    return false;
                }
                ++cc;
                if (nums[i] >= old_maxval) {
                    maxval = nums[i];
                }
            }
        }
        
        return true;
    }
};
