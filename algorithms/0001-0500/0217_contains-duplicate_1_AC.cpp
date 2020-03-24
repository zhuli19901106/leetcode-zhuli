#include <unordered_set>
using std::unordered_set;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> hash;
        int n = nums.size();
        int i;
        for (i = 0; i < n; ++i) {
            if (hash.find(nums[i]) != hash.end()) {
                return true;
            }
            hash.insert(nums[i]);
        }
        return false;
    }
};
