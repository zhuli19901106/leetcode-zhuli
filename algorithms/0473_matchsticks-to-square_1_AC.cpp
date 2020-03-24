#include <algorithm>
#include <cstdlib>
using std::max;
using std::rand;
using std::sort;

bool comparator(const int &i1, const int &i2)
{
    return i1 > i2;
}

class Solution {
public:
    bool makesquare(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) {
            return false;
        }
        
        int i;
        int sum = 0;
        int max_val = 0;
        for (i = 0; i < n; ++i) {
            sum += nums[i];
            max_val = max(max_val, nums[i]);
        }
        if (sum % 4 != 0 || max_val > sum / 4) {
            return false;
        }
        
        vector<int> sides(4, 0);
        sort(nums.begin(), nums.end(), comparator);
        return dfs(0, sides, nums, sum / 4);
    }
private:
    bool dfs(int idx, vector<int> &sides, vector<int> &nums, int target) {
        if (idx == nums.size()) {
            return true;
        }
        int i;
        for (i = 0; i < 4; ++i) {
            if (sides[i] + nums[idx] > target) {
                continue;
            }
            sides[i] += nums[idx];
            if(dfs(idx + 1, sides, nums, target)) {
                return true;
            }
            sides[i] -= nums[idx];
        }
        return false;
    }
};
