#include <algorithm>
using std::sort;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        int n = nums.size();
        if (n < 3) {
            return res;
        }
        sort(nums.begin(), nums.end());
        
        vector<int> t(3);
        int i, j, k;
        int val;
        
        i = 0;
        while (i < n && nums[i] <= 0) {
            t[0] = nums[i];
            j = i + 1;
            k = n - 1;
            while (j < k) {
                val = nums[i] + nums[j] + nums[k];
                if (val < 0) {
                    ++j;
                    continue;
                }
                if (val > 0) {
                    --k;
                    continue;
                }
                t[1] = nums[j];
                t[2] = nums[k];
                res.push_back(t);
                while (j + 1 < k && nums[j] == nums[j + 1]) {
                    ++j;
                }
                ++j;
            }
            // Skip duplicate results
            while (i + 1 < n && nums[i] == nums[i + 1]) {
                ++i;
            }
            ++i;
        }
        
        return res;
    }
};
