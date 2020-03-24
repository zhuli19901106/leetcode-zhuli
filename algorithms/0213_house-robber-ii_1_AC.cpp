#include <algorithm>
using std::max;

class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) {
            return nums[0];
        }
        return max(solve(nums, 0, n - 2), solve(nums, 1, n - 1));
    }
private:
    int solve(vector<int> & nums, int left, int right) {
        int n = right - left + 1;
        if (n <= 0) {
            return 0;
        } else if (n == 1) {
            return nums[left];
        } else if (n == 2) {
            return max(nums[left], nums[right]);
        }
        int i;
        int n1, n2, n3;
        n1 = nums[left];
        n2 = max(n1, nums[left + 1]);
        for (i = left + 2; i <= right; ++i) {
            n3 = max(n2, nums[i] + n1);
            n1 = n2;
            n2 = n3;
        }
        return n2;
    }
};
