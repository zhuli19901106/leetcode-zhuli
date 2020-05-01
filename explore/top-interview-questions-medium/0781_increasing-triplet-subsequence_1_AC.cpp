#include <climits>

class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int n = nums.size();
        int i;
        int a1, a2;
        
        a1 = a2 = INT_MAX;
        for (i = 0; i < n; ++i) {
            if (nums[i] == a1) {
                continue;
            }
            if (nums[i] < a1) {
                a1 = nums[i];
            } else if (nums[i] > a2) {
                return true;
            } else {
                a2 = nums[i];
            }
        }
        return false;
    }
};
