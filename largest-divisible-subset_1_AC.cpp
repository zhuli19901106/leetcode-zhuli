#include <algorithm>
using std::sort;

class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) {
            return nums;
        }
        sort(nums.begin(), nums.end());
        
        vector<int> dp(n);
        vector<int> bt(n);
        int i;
        for (i = 0; i < n; ++i) {
            dp[i] = 1;
            bt[i] = i;
        }
        int j;
        for (i = 1; i < n; ++i) {
            for (j = i - 1; j >= 0; --j) {
                if (nums[i] % nums[j] != 0) {
                    continue;
                }
                if (dp[i] < dp[j] + 1) {
                    dp[i] = dp[j] + 1;
                    bt[i] = j;
                }
            }
        }
        int mi = 0;
        for (i = 1; i < n; ++i) {
            if (dp[i] > dp[mi]) {
                mi = i;
            }
        }
        
        vector<int> res;
        while (true) {
            res.push_back(nums[mi]);
            if (bt[mi] == mi) {
                break;
            } else {
                mi = bt[mi];
            }
        }
        reverse(res.begin(), res.end());
        dp.clear();
        bt.clear();
        return res;
    }
};
