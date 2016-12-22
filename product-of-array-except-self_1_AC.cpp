class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n);
        if (n <= 0) {
            return res;
        }
        
        int i;
        int product;
        
        product = 1;
        for (i = n - 1; i >= 0; --i) {
            res[i] = product;
            product *= nums[i];
        }
        product = 1;
        for (i = 0; i <= n - 1; ++i) {
            res[i] *= product;
            product *= nums[i];
        }
        return res;
    }
};
