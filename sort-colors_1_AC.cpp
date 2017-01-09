// Some algorithmic problems are just boring, as if they lived only to serve in an interview.
// 小生有一句脏话，不知当讲不当讲？
#include <algorithm>
using std::min;
using std::swap;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        int i = 0;
        int j = n - 1;
        int k = n - 1;
        while (i <= j) {
            if (nums[i] == 1) {
                swap(nums[i], nums[j--]);
            } else if (nums[i] == 2) {
                swap(nums[i], nums[k--]);
                j = min(j, k);
            } else {
                ++i;
            }
        }
    }
};
