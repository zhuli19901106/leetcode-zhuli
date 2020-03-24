#include <algorithm>
#include <unordered_map>
using std::max;
using std::unordered_map;

class Solution {
public:
    int maxSubArrayLen(vector<int>& nums, int k) {
        unordered_map<int, int> um;
        int n = nums.size();
        
        int res = 0;
        int s = 0;
        int i;
        um[0] = 0;
        for (i = 0; i < n; ++i) {
            s += nums[i];
            if (um.find(s - k) != um.end()) {
                res = max(res, i + 1 - um[s - k]);
            }
            if (um.find(s) == um.end()) {
                um[s] = i + 1;
            }
        }
        um.clear();
        
        return res;
    }
};
