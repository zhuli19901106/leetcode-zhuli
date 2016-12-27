// Think from a bit's perspective
#include <unordered_map>
using std::unordered_map;

class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        unordered_map<int, int> um;
        int n = nums.size();
        int i;
        int x;
        for (i = 0; i < n; ++i) {
            x = nums[i];
            while (x != 0) {
                ++um[x & -x];
                x = x & x - 1;
            }
        }
        
        unordered_map<int, int>::const_iterator it;
        int res = 0;
        for (it = um.begin(); it != um.end(); ++it) {
            res += it->second * (n - it->second);
        }
        um.clear();
        
        return res;
    }
};
