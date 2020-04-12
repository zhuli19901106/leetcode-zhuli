class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int n = nums.size();
        int i;
        int res = 0;
        for (i = 0; i < n; ++i) {
            res ^= nums[i];
        }
        return res;
    }
};
