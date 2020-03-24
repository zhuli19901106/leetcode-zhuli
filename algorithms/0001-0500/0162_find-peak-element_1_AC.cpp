class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n = nums.size();
        int i;
        for (i = 0; i < n - 1; ++i) {
            if (nums[i] > nums[i + 1]) {
                break;
            }
        }
        return i;
    }
};
