#include <unordered_map>
using std::unordered_map;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int n = nums.size();
        if (n == 0) {
            return 0;
        }
        
        vector<unordered_map<int, int>> um(2);
        int f, nf;
        int mult = 1;
        int i;
        
        um[0][0] = 1;
        f = 1;
        nf = !f;
        for (i = 0; i < n; ++i) {
            if (nums[i] == 0) {
                mult <<= 1;
                continue;
            }
            um[f].clear();
            for (auto it = um[nf].begin(); it != um[nf].end(); ++it) {
                um[f][it->first - nums[i]] += it->second;
                um[f][it->first + nums[i]] += it->second;
            }
            f = !f;
            nf = !f;
        }
        int res = um[nf][S] * mult;
        um.clear();
        return res;
    }
};
