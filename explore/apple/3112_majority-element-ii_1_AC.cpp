class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n = nums.size();
        int i;
        int n1, n2;
        int c1, c2;
        
        c1 = c2 = 0;
        for (i = 0; i < n; ++i) {
            if (nums[i] == n1) {
                ++c1;
            } else if (nums[i] == n2) {
                ++c2;
            } else if (c1 == 0) {
                n1 = nums[i];
                c1 = 1;
            } else if (c2 == 0) {
                n2 = nums[i];
                c2 = 1;
            } else {
                --c1;
                --c2;
            }
        }
        c1 = c2 = 0;
        for (i = 0; i < n; ++i) {
            if (nums[i] == n1) {
                ++c1;
            } else if (nums[i] == n2) {
                ++c2;
            }
        }
        vector<int> res;
        if (c1 > n / 3) {
            res.push_back(n1);
        }
        if (c2 > n / 3) {
            res.push_back(n2);
        }
        return res;
    }
};
