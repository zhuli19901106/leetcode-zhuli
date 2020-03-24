#include <unordered_map>
#include <vector>
using std::unordered_map;
using std::vector;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        auto &a = nums;
        int n = a.size();
        unordered_map<int, int> um;
        ++um[0];
        
        int i;
        int sum = 0;
        int res = 0;
        for (i = 0; i < n; ++i) {
            sum += a[i];
            if (um.find(sum - k) != um.end()) {
                res += um[sum - k];
            }
            ++um[sum];
        }
        um.clear();
        return res;
    }
};
