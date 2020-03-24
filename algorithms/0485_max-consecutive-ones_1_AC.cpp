#include <algorithm>
using std::max;

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int n = nums.size();
        int i, j;
        int res = 0;
        
        i = 0;
        while (i < n) {
            if (nums[i] == 0) {
                ++i;
                continue;
            }
            j = i + 1;
            while (j < n && nums[j] == 1) { 
                ++j;
            }
            res = max(res, j - i);
            i = j;
        }
        return res;
    }
};
