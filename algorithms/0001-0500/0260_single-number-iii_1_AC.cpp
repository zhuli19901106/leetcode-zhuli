class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int sum = 0;
        int n = nums.size();
        int i;
        for (i = 0; i < n; ++i) {
            sum ^= nums[i];
        }
        sum = sum & -sum;
        int n1 = 0;
        int n2 = 0;
        for (i = 0; i < n; ++i) {
            if (nums[i] & sum) {
                n1 ^= nums[i];
            } else {
                n2 ^= nums[i];
            }
        }
        vector<int> res;
        res.push_back(n1);
        res.push_back(n2);
        return res;
    }
};
