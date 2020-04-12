class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        int i, j;
        i = j = 0;
        while (i < n) {
            if (nums[i] != 0) {
                nums[j++] = nums[i];
            }
            ++i;
        }
        while (j < n) {
            nums[j++] = 0;
        }
    }
};
