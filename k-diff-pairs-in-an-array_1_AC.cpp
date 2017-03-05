#include <unordered_set>
#include <vector>
using std::unordered_set;
using std::vector;

class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        if (k < 0) {
            return 0;
        }
        unordered_set<int> us, dup;
        int n = nums.size();
        int i;
        for (i = 0; i < n; ++i) {
            if (us.find(nums[i]) == us.end()) {
                us.insert(nums[i]);
            } else {
                dup.insert(nums[i]);
            }
        }
        int res = 0;
        for (auto it = us.begin(); it != us.end(); ++it) {
            if (k == 0 && dup.find(*it + k) != dup.end()) {
                ++res;
            }
            if (k != 0 && us.find(*it + k) != us.end()) {
                ++res;
            }
        }
        us.clear();
        dup.clear();
        
        return res;
    }
};
