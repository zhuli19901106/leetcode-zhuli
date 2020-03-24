// I'm getting bored of this.
#include <algorithm>
#include <vector>
using std::max;
using std::vector;

class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int n = nums.size();
        int i, j;
        int res = 0;
        i = 0;
        while (i < n) {
            j = i + 1;
            while (j < n && nums[j] > nums[j - 1]) {
                ++j;
            }
            res = max(res, j - i);
            i = j;
        }
        return res;
    }
};
