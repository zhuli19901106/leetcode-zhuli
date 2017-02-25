#include <algorithm>
#include <utility>
#include <unordered_map>
#include <vector>
using std::make_pair;
using std::max;
using std::pair;
using std::unordered_map;
using std::vector;

class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int sum = 0;
        int n = nums.size();
        unordered_map<int, pair<int, int>> um;
        um[0] = make_pair(0, 0);
        
        int i;
        for (i = 1; i <= n; ++i) {
            sum += (nums[i - 1] == 1 ? 1 : -1);
            if (um.find(sum) == um.end()) {
                um[sum] = make_pair(i, i);
            } else {
                um[sum].second = i;
            }
        }
        int res = 0;
        for (auto it = um.begin(); it != um.end(); ++it) {
            res = max(res, it->second.second - it->second.first);
        }
        um.clear();
        
        return res;
    }
};
