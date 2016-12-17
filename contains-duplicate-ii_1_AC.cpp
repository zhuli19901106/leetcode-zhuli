#include <unordered_map>
using std::unordered_map;

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        if (k <= 0) {
            return false;
        }
        
        unordered_map<int, int> um;
        int n = nums.size();
        int i = 0;
        while (i < k + 1 && i < n) {
            if (um.find(nums[i]) != um.end()) {
                return true;
            } else {
                um[nums[i]] = i;
                ++i;
            }
        }
        while (i < n) {
            um.erase(nums[i - k - 1]);
            if (um.find(nums[i]) != um.end()) {
                return true;
            } else {
                um[nums[i]] = i;
                ++i;
            }
        }
        return false;
    }
};
