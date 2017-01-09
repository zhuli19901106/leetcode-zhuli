// Power set
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> v;
        int n = nums.size();
        int m = 1 << n;
        int i, j, bit;
        for (i = 0; i < m; ++i) {
            bit = i;
            for (j = 0; j < n; ++j) {
                if (bit & 1) {
                    v.push_back(nums[j]);
                }
                bit >>= 1;
            }
            res.push_back(v);
            v.clear();
        }
        
        return res;
    }
};
