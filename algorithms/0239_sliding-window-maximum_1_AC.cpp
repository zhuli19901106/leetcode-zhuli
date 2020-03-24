#include <algorithm>
#include <map>
#include <vector>
using std::map;
using std::min;
using std::vector;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        int n = nums.size();
        if (n == 0) {
            return res;
        }
        k = min(k, n);
        
        map<int, int> mm;
        int i;
        for (i = 0; i < k - 1; ++i) {
            ++mm[nums[i]];
        }
        ++mm[nums[i]];
        res.push_back(mm.rbegin()->first);
        
        for (i = k; i < n; ++i) {
            --mm[nums[i - k]];
            if (mm[nums[i - k]] == 0) {
                mm.erase(nums[i - k]);
            }
            ++mm[nums[i]];
            res.push_back(mm.rbegin()->first);
        }
        mm.clear();
        
        return res;
    }
};
