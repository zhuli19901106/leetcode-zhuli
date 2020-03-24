#include <algorithm>
using std::lower_bound;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> seq;
        int n = nums.size();
        if (n < 2) {
            return n;
        }
        seq.push_back(nums[0]);
        
        int i;
        int j;
        for (i = 1; i < n; ++i) {
            if (nums[i] > seq.back()) {
                seq.push_back(nums[i]);
                continue;
            }
            j = lower_bound(seq.begin(), seq.end(), nums[i]) - seq.begin();
            seq[j] = nums[i];
        }
        int res = seq.size();
        seq.clear();
        return res;
    }
};
