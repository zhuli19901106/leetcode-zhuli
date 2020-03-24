class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int n = nums.size();
        int res = 0;
        int cnt;
        int i, j;
        for (i = 0; i < 32; ++i) {
            cnt = 0;
            for (j = 0; j < n; ++j) {
                if ((nums[j] & (1 << i)) != 0) {
                    ++cnt;
                }
            }
            if (cnt % 3 != 0) {
                res |= (1 << i);
            }
        }
        return res;
    }
};
