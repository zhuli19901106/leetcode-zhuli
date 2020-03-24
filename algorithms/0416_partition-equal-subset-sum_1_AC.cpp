class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int n = nums.size();
        int i;
        int sum = 0;
        for (i = 0; i < n; ++i) {
            sum += nums[i];
        }
        if (sum & 1) {
            return false;
        }
        sum >>= 1;
        
        int j;
        vector<bool> dp(sum + 1, false);
        dp[0] = true;
        for (i = 0; i < n; ++i) {
            for (j = sum; j >= nums[i]; --j) {
                dp[j] = (dp[j] || dp[j - nums[i]]);
            }
        }
        bool res = dp[sum];
        dp.clear();
        
        return res;
    }
};
