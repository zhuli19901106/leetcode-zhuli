// A wonderful solution from user @tangx668
// I got stuck on this problem. Just couldn't get the inspiration.
#include <unordered_set>
using std::unordered_set;

class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        unordered_set<int> us;
        unordered_set<int>::const_iterator it;
        int n = nums.size();
        int i, j;
        int val;
        int mask;
        int res;
        
        mask = 0;
        res = 0;
        for (i = 31; i >= 0; --i) {
            mask |= (1 << i);
            for (j = 0; j < n; ++j) {
                us.insert(mask & nums[j]);
            }
            val = res | (1 << i);
            for (it = us.begin(); it != us.end(); ++it) {
                if (us.find(val ^ *it) != us.end()) {
                    res = val;
                    break;
                }
            }
            us.clear();
        }
        return res;
    }
};
